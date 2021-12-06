class Board:
    coordinates = {}

    def mark_line(self, x1, y1, x2, y2):
        print(f'Line: {x1}, {y1} -> {x2}, {y2}')
        if x1 == x2:
            for i in range(abs(y2 - y1) + 1):
                smaller = y1 if y1 < y2 else y2
                self.mark_point(x1, i + smaller)
        elif y1 == y2:
            for i in range(abs(x2 - x1) + 1):
                smaller = x1 if x1 < x2 else x2
                self.mark_point(i + smaller, y1)
        else:
            if x1 > x2 and y1 > y2:
                for i in range(abs(y1 - y2) + 1):
                    self.mark_point(x2 + i, y2 + i)
            elif x1 < x2 and y1 < y2:
                for i in range(abs(y2 - y1) + 1):
                    self.mark_point(x1 + i, y1 + i)
            elif x1 > x2 and y1 < y2:
                for i in range(abs(x1 - x2) + 1):
                    self.mark_point(x2 + i, y2 - i)
            elif x1 < x2 and y1 > y2:
                for i in range(abs(y1 - y2) + 1):
                    self.mark_point(x1 + i, y1 - i)

    def mark_point(self, x, y):
        key = f'{x}-{y}'
        if key in self.coordinates:
            self.coordinates[key] += 1
        else:
            self.coordinates[key] = 1

    def get_overlap_number(self):
        overlap_number = 0
        for k, v in self.coordinates.items():
            if v > 1:
                overlap_number += 1
        return overlap_number


def main():
    with open('data.txt', 'r') as f:
        lines = f.readlines()
        b = Board()
        for line in lines:
            p1, arrow, p2 = line.strip().split()
            x1, y1 = p1.split(',')
            x2, y2 = p2.split(',')
            b.mark_line(int(x1), int(y1), int(x2), int(y2))
        print(b.get_overlap_number())


if __name__ == '__main__':
    main()
