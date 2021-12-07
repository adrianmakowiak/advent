from statistics import median


def main():
    with open('data.txt', 'r') as f:
        data = f.readline()
        crabs_position = [int(pos) for pos in data.strip().split(',')]
        average = median(crabs_position)

        print(average)
        fuel_used = 0
        for pos in crabs_position:
            fuel_used += abs(average - pos)
        print(fuel_used)


if __name__ == '__main__':
    main()
