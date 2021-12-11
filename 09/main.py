from statistics import mean
def check_neighbour(x, y, value, locations):
    if x < 0 or y < 0:
        return True
    try:
        if locations[x][y] > value:
            return True
        else:
            return False
    except IndexError:
        return True


def main():
    with open('input.txt', 'r') as f:
        data = f.readlines()
        locations = []
        for line in data:
            row = line.strip()
            row_numbers = [int(n) for n in row]
            locations.append(row_numbers)
        numbers = []
        sum = 0
        print(locations[26][0])
        print(locations[26][0])
        for i, row in enumerate(locations):

            # print(row)
            # print(len(row))
            for j, value in enumerate(row):
                # print(locations[i][j])
                if check_neighbour(i-1, j, value, locations) and check_neighbour(i+1, j, value, locations) and check_neighbour(i, j-1, value, locations) and check_neighbour(i, j+1, value, locations):
                    numbers.append(value)
                    sum += value + 1
                    print(sum)
                    # print(i,j, value)
        # print(numbers)
        # print(len(numbers))
        # # print(mean(numbers))
        # print(sum(map(lambda x: x+1, numbers)))


if __name__ == '__main__':
    main()
