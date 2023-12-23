from utils import PIPE_CHARS

PADDING_V = 1
PADDING_H = 2

def render_pipes(stdscr, pipes, num, reward):
    stdscr.clear()
    for i, p in enumerate(pipes):
        stdscr.addstr(
            PADDING_V + i,
            PADDING_H,
            "".join(p)
        )

    stdscr.addstr(
        PADDING_V + len(pipes) + 1,
        PADDING_H,
       f"Episode: {num}"
    )

    if reward is not None:
        stdscr.addstr(
            PADDING_V + len(pipes) + 2,
            PADDING_H,
        f"Reward: {reward}"
        )

    stdscr.refresh()



