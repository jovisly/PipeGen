import curses
import random

NUM_ROWS = 20
NUM_COLS = 40
PADDING_V = 1
PADDING_H = 2
PIPE_CHARS = ["═", "║", "╗", "╝", "╔", "╚", "╬"]
PIPE_DENSITY = 0.5

def render_pipes(stdscr):
    stdscr.clear()
    for h in range(NUM_COLS):
        for v in range(NUM_ROWS):
            if random.random() < PIPE_DENSITY:
                stdscr.addstr(
                    v + PADDING_V,
                    h + PADDING_H,
                    random.choice(PIPE_CHARS)
                )

    stdscr.refresh()
    stdscr.getch()


curses.wrapper(render_pipes)
