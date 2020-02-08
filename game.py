import numpy as np

TAG_END = "+-----------------------------------------------------------+"
COLUMN_SEPARATOR = "|              |              |              |              |"
EMPTY_ROW = [0, 0, 0, 0]


class Game:
    def __init__(self, numbers):
        self.numbers = np.array(numbers)

    def draw(self):
        board = [TAG_END]
        total = len(self.numbers)
        for i in range(0, total):
            a, b, c, d = self.center(*self.numbers[i])
            board.append(COLUMN_SEPARATOR)
            board.append("|" + a + "|" + b + "|" + c + "|" + d + "|")
            board.append(COLUMN_SEPARATOR)
            board.append(TAG_END)
        return board

    def up(self):
        numbers = self.calculate_table(np.rot90(self.numbers, 2))
        self.numbers = np.rot90(numbers, 2)

    def down(self):
        return self.calculate_table(self.numbers)

    def right(self):
        numbers = self.calculate_table(np.rot90(self.numbers, -1))
        self.numbers = np.rot90(numbers)

    def left(self):
        numbers = self.calculate_table(np.rot90(self.numbers))
        self.numbers = np.rot90(numbers, -1)

    @staticmethod
    def calculate_table(numbers):
        for i in range(0, 3):
            down_row = np.array(numbers[i + 1])
            current = np.array(numbers[i])
            if np.array_equal(down_row, np.array(EMPTY_ROW)):
                numbers[i + 1] = current
                numbers[i] = EMPTY_ROW
                continue
            for j in range(0, 4):
                if current[j] == down_row[j]:
                    down_row[j] += current[j]
                    current[j] = 0
                elif down_row[j] == 0:
                    down_row[j] = current[j]
                    current[j] = 0
                else:
                    if i + 2 < len(numbers):
                        numbers[i + 2][j] = down_row[j]
                        down_row[j] = current[j]
                        current[j] = 0

            numbers[i + 1] = down_row
            numbers[i] = current

        return numbers

    @staticmethod
    def center(a, b, c, d):
        a = str(a) if a > 0 else ""
        b = str(b) if b > 0 else ""
        c = str(c) if c > 0 else ""
        d = str(d) if d > 0 else ""
        return a.center(14), b.center(14), c.center(14), d.center(14)
