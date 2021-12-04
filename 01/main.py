def main():
    with open('data.txt', 'r') as f:
        previous = None
        counter = 0
        for line in f:
            current = int(line)
            if previous and current > previous:
                counter += 1
            previous = current
        print(counter)


def main2():
    with open('data.txt', 'r') as f:
        previous = None
        counter = 0
        values = [int(line) for line in f.readlines()]
        for i in range(len(values) - 2):
            current = values[i] + values[i+1] + values[i+2]
            if previous and current > previous:
                counter += 1
            previous = current
        print(counter)


if __name__ == '__main__':
    main2()

