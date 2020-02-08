import numpy as np

TAG_END = "+-----------------------------------------------------------+"
COLUMN_SEPARATOR = "|              |              |              |              |"
EMPTY_ROW = [0, 0, 0, 0]


class Game:
    def __init__(self, numbers):
        self.numbers = np.array(numbers)
        self.score = 0

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
        numbers, score = self.calculate_table(np.rot90(self.numbers, 2))
        self.score += score
        self.numbers = np.rot90(numbers, 2)

    def down(self):
        numbers, score = self.calculate_table(self.numbers)
        self.score += score
        self.numbers = numbers

    def right(self):
        numbers, score = self.calculate_table(np.rot90(self.numbers, -1))
        self.score += score
        self.numbers = np.rot90(numbers)

    def left(self):
        numbers, score = self.calculate_table(np.rot90(self.numbers))
        self.score += score
        self.numbers = np.rot90(numbers, -1)

    @staticmethod
    def calculate_table(numbers):
        score = 0
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
                    score += down_row[j]
                    current[j] = 0
                elif down_row[j] == 0:
                    down_row[j] = current[j]
                    current[j] = 0
                elif i + 2 < len(numbers):
                    if numbers[i + 2][j] == 0:
                        numbers[i + 2][j] = down_row[j]
                        down_row[j] = current[j]
                    elif down_row[j] == numbers[i + 2][j]:
                        numbers[i + 2][j] += down_row[j]
                        score += numbers[i + 2][j]
                        down_row[j] = current[j]
                    current[j] = 0

            numbers[i + 1] = down_row
            numbers[i] = current

        return numbers, score

    @staticmethod
    def center(a, b, c, d):
        a = str(a) if a > 0 else ""
        b = str(b) if b > 0 else ""
        c = str(c) if c > 0 else ""
        d = str(d) if d > 0 else ""
        return a.center(14), b.center(14), c.center(14), d.center(14)
