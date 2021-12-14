from collections import Counter
from pprint import pprint

def main():
    with open('data.txt', 'r') as f:
        data = f.readlines()
        points = []
        instructions = []
        for line in data:
            if ',' in line:
                x, y = line.strip().split(',')
                points.append([int(x), int(y)])
            elif '=' in line:
                ax, level = line.strip().split()[2].split('=')
                instructions.append([ax, int(level)])

        point_set = set([f'{p[0]}-{p[1]}' for p in points])
        print(point_set)
        inst = instructions[0]
        print(len(point_set))
        for inst in instructions:
            new_set = set()
            if inst[0] == 'x':
                for point in point_set:
                    print(point)
                    a, b = point.split('-')
                    x = int(a)
                    y = int(b)
                    if x > inst[1]:
                        new_set.add(f'{inst[1] - (x - inst[1])}-{y}')
                    else:
                        new_set.add(point)
            elif inst[0] == 'y':
                for point in point_set:
                    print(point)
                    a, b = point.split('-')
                    x = int(a)
                    y = int(b)
                    if y > inst[1]:
                        new_set.add(f'{x}-{inst[1] - (y - inst[1])}')
                    else:
                        new_set.add(point)
            point_set = new_set.copy()
            print(point_set)

        print(point_set)
        print(len(point_set))

        result = ''

        tmp = 0
        for i in range(38):
            for j in range(6):
                if f'{i}-{j}' in point_set:
                    result += '#'
                else:
                    result += '.'

            result += '\n'


if __name__ == '__main__':
    main()
