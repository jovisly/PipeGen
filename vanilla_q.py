"""Q Learning for Pipe Generation.

State space: Each cell has four neighbors, and each neighbor has 8 possibilities,
so that's 4 x 8 = 32 states.

Action space: Each cell has 8 possible actions (the 8 configurations).

Organization: We will construct Q Table as a dictionary, keyed on the tuple of
(u, d, l, r), (a), where u is the cell above, d is the cell below, l is the cell
to the left, and r is the cell to the right. "a" is the action taken which is
the cell in the middle.
"""
from curses import wrapper
import random

from utils import PIPE_CHARS, ALLOWED_CONFIG
from viz import render_pipes

LEARNING_RATE = 0.8
DISCOUNT_FACTOR = 0.8
NUM_EPISODES = 100000
BATCH_SIZE = 10

NUM_ROWS = 20
NUM_COLS = 40


def get_state(pipes, row, col):
    u = pipes[row - 1][col] if row > 0 else " "
    d = pipes[row + 1][col] if row < NUM_ROWS - 1 else " "
    l = pipes[row][col - 1] if col > 0 else " "
    r = pipes[row][col + 1] if col < NUM_COLS - 1 else " "
    return (u, d, l, r)


def calculate_reward(s, a):
    """Calculate reward for taking action a in state s."""
    allowed = ALLOWED_CONFIG[a]
    reward = 0

    for i, dir in enumerate(["u", "d", "l", "r"]):
        if s[i] in allowed[dir]:
            reward += 1

    return reward


def calculate_total_reward(pipes):
    reward = 0
    for row in range(len(pipes)):
        for col in range(len(pipes[0])):
            s = get_state(pipes, row, col)
            a = pipes[row][col]

            # Calculate reward.
            reward += calculate_reward(s, a)


    return reward


def make_pipes(num_rows=NUM_ROWS, num_cols=NUM_COLS, density=0.5):
    non_empty_pipe_chars = [c for c in PIPE_CHARS if c != " "]
    pipes = []
    for _ in range(num_rows):
        row = []
        for _ in range(num_cols):
            if random.random() < density:
                row.append(random.choice(non_empty_pipe_chars))
            else:
                row.append(" ")
        pipes.append(row)

    return pipes



class QLearner:
    def __init__(self):
        self.q_table = {
            (u, d, l, r): {a: 0 for a in PIPE_CHARS}
            for u in PIPE_CHARS
            for d in PIPE_CHARS
            for l in PIPE_CHARS
            for r in PIPE_CHARS
        }


    def update(self, s, a):
        """Update follows Bellman equation."""
        prev_q = self.q_table[s][a]
        r = calculate_reward(s, a)
        self.q_table[s][a] = (
            prev_q +
            LEARNING_RATE * (
                r + DISCOUNT_FACTOR * max(self.q_table[s].values()) - prev_q
            )
        )


    def greedy_policy(self, s):
        return max(self.q_table[s], key=self.q_table[s].get)


    def epsilon_greedy_policy(self, s, epsilon):
        if random.random() < epsilon:
            return random.choice(PIPE_CHARS)
        else:
            return self.greedy_policy(s)


    def train(self, pipes, epsilon):
        # Choose a random cell.
        row = random.randint(0, NUM_ROWS - 1)
        col = random.randint(0, NUM_COLS - 1)
        s = get_state(pipes, row, col)

        # Choose a new cell using epsilon greedy policy.
        a = self.epsilon_greedy_policy(s, epsilon)
        pipes[row][col] = a

        # Update Q table.
        self.update(s, a)



def mini_tests():
    # (u, d, l, r)
    s = ("║", "╗", "╝", "╔")
    a = " "
    assert calculate_reward(s, a) == 3



def main(stdscr):
    mini_tests()
    # Initialize pipes.
    pipes = make_pipes()
    # Initialize learner.
    learner = QLearner()

    # Iteratively updates.
    for n in range(NUM_EPISODES):
        for _ in range(BATCH_SIZE):
            # With annealing.
            learner.train(pipes, epsilon=(1 - n / NUM_EPISODES))

        # Render.
        if (n + 1) % 1000 == 0:
            r = calculate_total_reward(pipes)
            render_pipes(stdscr, pipes, n + 1, r)

    stdscr.getch()



wrapper(main)
