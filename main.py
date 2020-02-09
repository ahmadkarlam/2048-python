import curses
import json
import random
from curses import wrapper

from game import Game


def main(stdscr):
    numbers = [[0, 8, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 16, 2, 2]]
    game = Game(numbers)
    last_key = ""
    empty = {}

    while True:
        _board = game.draw()
        stdscr.addstr("\n".join(_board))
        stdscr.addstr("\nscore: " + str(game.score))
        stdscr.addstr("\nempty cell: " + str(empty))
        stdscr.addstr("\nkey: " + last_key)

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
        # record last move
        game.add_recent_move(last_key)

        empties = game.get_empty_cell()
        index = random.randint(0, len(empties) - 1)
        empty = empties[index]
        game.fill_empty(random.choice([2, 4]), empty["i"], empty["j"])

        stdscr.clear()

    curses.endwin()
    return game.recent_moves


recent_moves = wrapper(main)
with open('movements.json', 'w') as fp:
    json.dump(recent_moves, fp)
