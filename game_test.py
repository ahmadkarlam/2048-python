import unittest
import numpy as np

from game import Game


class TestGame(unittest.TestCase):
    def test_up_move(self):
        tests = [{
            "name": "Test case 1",
            "args": [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 16, 2, 2]
            ],
            "expected": [
                [0, 16, 2, 2],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
        }, {
            "name": "Test case 2",
            "args": [
                [0, 0, 0, 2],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 16, 2, 2]
            ],
            "expected": [
                [0, 16, 2, 4],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
        }, {
            "name": "Test case 3",
            "args": [
                [0, 8, 2, 2],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 16, 2, 2]
            ],
            "expected": [
                [0, 8, 4, 4],
                [0, 16, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
        }, {
            "name": "Test case 4",
            "args": [
                [0, 8, 2, 2],
                [0, 4, 0, 0],
                [0, 0, 0, 0],
                [0, 16, 2, 2],
            ],
            "expected": [
                [0, 8, 4, 4],
                [0, 4, 0, 0],
                [0, 16, 0, 0],
                [0, 0, 0, 0],
            ],
        }]

        for test in tests:
            with self.subTest(test["name"]):
                print(test["name"])
                game = Game(test["args"])
                game.up()
                actual = game.numbers
                self.assertTrue(np.array_equal(actual, test["expected"]))

    def test_down_move(self):
        tests = [
            {
                "name": "Test case 1",
                "args": [
                    [0, 16, 2, 2],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                ],
                "expected": [
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 16, 2, 2],
                ]
            },
            {
                "name": "Test case 2",
                "args": [
                    [0, 16, 2, 2],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 2],
                ],
                "expected": [
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 16, 2, 4],
                ]
            },
            {
                "name": "Test case 3",
                "args": [
                    [0, 16, 2, 2],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 4, 2],
                ],
                "expected": [
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 2, 0],
                    [0, 16, 4, 4],
                ]
            },
            {
                "name": "Test case 4",
                "args": [
                    [0, 16, 2, 2],
                    [0, 0, 0, 0],
                    [0, 4, 0, 0],
                    [0, 8, 2, 2],
                ],
                "expected": [
                    [0, 0, 0, 0],
                    [0, 16, 0, 0],
                    [0, 4, 0, 0],
                    [0, 8, 4, 4],
                ],
            }
        ]

        for test in tests:
            with self.subTest(test["name"]):
                print(test["name"])
                game = Game(test["args"])
                game.down()
                actual = game.numbers
                self.assertTrue(np.array_equal(actual, test["expected"]))

    def test_right_move(self):
        tests = [{
            "name": "Test case 1",
            "args": [
                [0, 0, 0, 0],
                [16, 0, 0, 0],
                [2, 0, 0, 0],
                [2, 0, 0, 0],
            ],
            "expected": [
                [0, 0, 0, 0],
                [0, 0, 0, 16],
                [0, 0, 0, 2],
                [0, 0, 0, 2],
            ]
        }, {
            "name": "Test case 2",
            "args": [
                [0, 0, 0, 0],
                [16, 0, 0, 0],
                [2, 0, 0, 0],
                [2, 0, 0, 2],
            ],
            "expected": [
                [0, 0, 0, 0],
                [0, 0, 0, 16],
                [0, 0, 0, 2],
                [0, 0, 0, 4],
            ]
        }, {
            "name": "Test case 3",
            "args": [
                [0, 0, 0, 0],
                [16, 0, 0, 2],
                [2, 0, 0, 2],
                [2, 0, 0, 2],
            ],
            "expected": [
                [0, 0, 0, 0],
                [0, 0, 16, 2],
                [0, 0, 0, 4],
                [0, 0, 0, 4],
            ]
        }]

        for test in tests:
            with self.subTest(test["name"]):
                game = Game(test["args"])
                print(test["name"])
                game.right()
                actual = game.numbers
                self.assertTrue(np.array_equal(actual, test["expected"]))

    def test_left_move(self):
        tests = [
            {
                "name": "Test case 1",
                "args": [
                    [0, 0, 0, 0],
                    [0, 0, 0, 16],
                    [0, 0, 0, 2],
                    [0, 0, 0, 2],
                ],
                "expected": [
                    [0, 0, 0, 0],
                    [16, 0, 0, 0],
                    [2, 0, 0, 0],
                    [2, 0, 0, 0],
                ]
            }, {
                "name": "Test case 2",
                "args": [
                    [0, 0, 0, 0],
                    [0, 0, 0, 16],
                    [0, 0, 0, 2],
                    [2, 0, 0, 2],
                ],
                "expected": [
                    [0, 0, 0, 0],
                    [16, 0, 0, 0],
                    [2, 0, 0, 0],
                    [4, 0, 0, 0],
                ]
            },
            {
                "name": "Test case 3",
                "args": [
                    [0, 0, 0, 0],
                    [0, 0, 16, 2],
                    [2, 0, 0, 2],
                    [2, 0, 0, 2],
                ],
                "expected": [
                    [0, 0, 0, 0],
                    [16, 2, 0, 0],
                    [4, 0, 0, 0],
                    [4, 0, 0, 0],
                ]
            }]

        for test in tests:
            with self.subTest(test["name"]):
                game = Game(test["args"])
                print(test["name"])
                game.left()
                actual = game.numbers
                self.assertTrue(np.array_equal(actual, test["expected"]))

    def test_movement_1(self):
        game = Game([
            [0, 8, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 16, 2, 2],
        ])
        game.down()
        actual = game.numbers
        self.assertTrue(np.array_equal(actual, [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 8, 0, 0],
            [0, 16, 4, 4],
        ]))

        game.right()
        actual = game.numbers
        self.assertTrue(np.array_equal(actual, [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 8],
            [0, 0, 16, 8],
        ]))

    def test_movement_2(self):
        game = Game([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 4, 2, 2],
            [0, 2, 16, 16],
        ])
        game.right()
        actual = game.numbers
        self.assertTrue(np.array_equal(actual, [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 4, 4],
            [0, 0, 2, 32],
        ]))


if __name__ == '__main__':
    unittest.main()
