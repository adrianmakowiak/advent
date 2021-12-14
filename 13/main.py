from collections import Counter
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
        new_set = set()
        if inst[0] == 'x':
            for point in point_set:
                a, b = point.split('-')
                x = int(a)
                y = int(b)
                if x > inst[1]:
                    new_set.add(f'{inst[1] - (x - inst[1])}-{y}')
                else:
                    new_set.add(point)

        print(len(new_set))
        # elif inst[0] == 'y':
        #     for x, y in points_dict.items():
        #         if y > inst[1]:
        #             dict_step[inst[1] - (y - inst[1])] = y
        #         else:
        #             dict_step[x] = y
        #

        # print(points)
        # print(instructions)
        # print(points_dict)
        # for inst in instructions:
        # #     print(inst)
        #
        # dict_step = {}

        # print(len(points_dict))
        # print(len(dict_step))

if __name__ == '__main__':
    main()
