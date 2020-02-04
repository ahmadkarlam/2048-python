TAG_END = "+-----------------------------------------------------------+"
COLUMN_SEPARATOR = "|              |              |              |              |"
EMPTY_ROW = [0, 0, 0, 0]


class Game:
    def __init__(self, numbers):
        self.numbers = numbers

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
        numbers = self.numbers
        for i in range(3, 0, -1):
            up_row = numbers[i - 1]
            current = numbers[i]
            if up_row == EMPTY_ROW:
                numbers[i - 1] = current
                numbers[i] = EMPTY_ROW
                continue

            for j in range(0, 4):
                if current[j] == up_row[j]:
                    up_row[j] += current[j]
                    current[j] = 0
                elif up_row[j] == 0:
                    up_row[j] = current[j]
                    current[j] = 0

            numbers[i - 1] = up_row
            numbers[i] = current

        self.numbers = numbers

    def down(self):
        numbers = self.numbers
        self.numbers = numbers

    def right(self):
        numbers = self.numbers
        self.numbers = numbers

    def left(self):
        numbers = self.numbers
        self.numbers = numbers

    @staticmethod
    def center(a, b, c, d):
        a = str(a) if a > 0 else ""
        b = str(b) if b > 0 else ""
        c = str(c) if c > 0 else ""
        d = str(d) if d > 0 else ""
        return a.center(14), b.center(14), c.center(14), d.center(14)
