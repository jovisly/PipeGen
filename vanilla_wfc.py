"""Wave Function Collapse.

This is a simple wave function collapse implementation where the rules are
defined in utils.py. Typically, the rules are inferred by an input image that
depicts typical patterns.
"""
import random
import time
from curses import wrapper

from utils import PIPE_CHARS, ALLOWED_CONFIG, PIPE_CHARS_WEIGHTS
from viz import render_pipes


NUM_ROWS = 20
NUM_COLS = 40


def make_pipes(num_rows=NUM_ROWS, num_cols=NUM_COLS):
    pipes = []
    for _ in range(num_rows):
        row = []
        for _ in range(num_cols):
            row.append("?")
        pipes.append(row)

    return pipes


def collapse_tile(pipes, row, col):
    u = pipes[row - 1][col] if row > 0 else " "
    d = pipes[row + 1][col] if row < NUM_ROWS - 1 else " "
    l = pipes[row][col - 1] if col > 0 else " "
    r = pipes[row][col + 1] if col < NUM_COLS - 1 else " "

    allowed_u = ALLOWED_CONFIG[u]["d"] if u != "?" else PIPE_CHARS
    allowed_d = ALLOWED_CONFIG[d]["u"] if d != "?" else PIPE_CHARS
    allowed_l = ALLOWED_CONFIG[l]["r"] if l != "?" else PIPE_CHARS
    allowed_r = ALLOWED_CONFIG[r]["l"] if r != "?" else PIPE_CHARS

    allowed = [
        pipe for pipe in PIPE_CHARS
        if pipe in allowed_u and pipe in allowed_d and pipe in allowed_l and pipe in allowed_r
    ]

    weights = [PIPE_CHARS_WEIGHTS[pipe] for pipe in allowed]

    if len(allowed) == 0:
        print("ERROR: CONTRADICTION")

    return random.choices(population=allowed, weights=weights)[0]



def main(stdscr):
    # Initialize pipes.
    pipes = make_pipes()
    # Pick the first location from one edge. This seems to be better at avoiding
    # contradictions than random.
    row = 0
    col = 0
    queue = [(row, col)]
    episode_num = 0

    while len(queue) > 0:
        time.sleep(0.01)
        episode_num += 1
        q = queue.pop(0)
        t = collapse_tile(pipes, *q)
        pipes[q[0]][q[1]] = t
        new_queues = [(q[0] - 1, q[1]), (q[0] + 1, q[1]), (q[0], q[1] - 1), (q[0], q[1] + 1)]
        for new_q in new_queues:
            if (
                new_q[0] >= 0 and
                new_q[0] < NUM_ROWS and
                new_q[1] >= 0 and
                new_q[1] < NUM_COLS
                and pipes[new_q[0]][new_q[1]] == "?"
                and new_q not in queue
            ):
                queue.append(new_q)


        render_pipes(stdscr, pipes, episode_num, None)
    stdscr.getch()


wrapper(main)
