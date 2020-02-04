import unittest

from game import Game


class TestGame(unittest.TestCase):
    def test_up_move(self):
        # Test case 1
        game = Game([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 16, 2, 2]])
        game.up()
        actual = game.numbers
        self.assertEqual(actual, [
            [0, 16, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]])

        # Test case 2
        game = Game([
            [0, 0, 0, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 16, 2, 2]])
        game.up()
        actual = game.numbers
        self.assertEqual(actual, [
            [0, 16, 2, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ])

        # Test case 3
        game = Game([
            [0, 8, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 16, 2, 2]])
        game.up()
        actual = game.numbers
        self.assertEqual(actual, [
            [0, 8, 4, 4],
            [0, 16, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ])

        # Test case 4
        game = Game([
            [0, 8, 2, 2],
            [0, 4, 0, 0],
            [0, 0, 0, 0],
            [0, 16, 2, 2]])
        game.up()
        actual = game.numbers
        self.assertEqual(actual, [
            [0, 8, 4, 4],
            [0, 4, 0, 0],
            [0, 16, 0, 0],
            [0, 0, 0, 0],
        ])


if __name__ == '__main__':
    unittest.main()
