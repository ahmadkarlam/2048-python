import curses
from curses import wrapper

from game import Game


def main(stdscr):
    numbers = [[0, 8, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 16, 2, 2]]
    game = Game(numbers)
    last_key = ""

    while True:
        _board = game.draw()
        stdscr.addstr("\n".join(_board))
        stdscr.addstr("\ndebug: " + last_key)

        c = stdscr.getch()
        if c == curses.KEY_UP:
            game.up()
            last_key = "up"
        elif c == curses.KEY_DOWN:
            game.down()
            last_key = "down"
        elif c == curses.KEY_RIGHT:
            game.right()
            last_key = "right"
        elif c == curses.KEY_LEFT:
            game.left()
            last_key = "left"
        elif c == ord("q"):
            break
        stdscr.clear()

    curses.endwin()


wrapper(main)
