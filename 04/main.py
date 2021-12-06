class Board:
    matrix = []
    bingo = []

    def __init__(self, rows):
        numbers = [row.split() for row in rows]
        self.matrix = numbers
        self.bingo = [number_row[:] for number_row in numbers]

    def mark_number(self, number):
        for i, rows in enumerate(self.bingo):
            for j, n in enumerate(rows):
                if n == number:
                    self.bingo[i][j] = -1
                    return self.check_if_won(i, j, number)
        return False

    def check_if_won(self, x, y, number):
        # check horizontal
        won = True
        for value in self.bingo[x]:
            if value != -1:
                won = False
                break
        if won:
            return True
        won = True
        for i in range(5):
            if self.bingo[i][y] != -1:
                won = False
                return False
        if won:
            return True

    def calculate_sum(self):
        sum_result = 0
        for i, row in enumerate(self.bingo):
            for j, cell in enumerate(self.bingo[i]):
                if self.bingo[i][j] != -1:
                    sum_result += int(self.matrix[i][j])
        return sum_result


def main():
    with open('data.txt', 'r') as f:
        numbers = f.readline()
        numbers = numbers.split(',')
        _ = f.readline()
        rest = f.readlines()
        boards = []
        rows = []
        for line in rest:
            if line == '\n':
                boards.append(Board(rows))
                rows = []
            else:
                rows.append(line.strip())
        for n in numbers:
            for b in boards:
                if b.mark_number(n):
                    sum_result = b.calculate_sum()
                    result = sum_result * int(n)
                    print(result)
                    return


if __name__ == '__main__':
    main()
