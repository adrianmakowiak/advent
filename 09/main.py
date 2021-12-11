import math

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


def traverse_rec(x, y, locations):
    # TRY UP
    rec_sum = 0
    try:
        if x == 0:
            pass
        elif locations[x-1][y] not in [-1, 9]:
            locations[x-1][y] = -1
            rec_sum += traverse_rec(x-1, y, locations) + 1
    except IndexError:
        pass
    # TRY RIGHT
    try:
        if locations[x][y+1] not in [-1, 9]:
            locations[x][y+1] = -1
            rec_sum += traverse_rec(x, y+1, locations) + 1
    except IndexError:
        pass
    # TRY DOWN
    try:
        if locations[x+1][y] not in [-1, 9]:
            locations[x+1][y] = -1
            rec_sum += traverse_rec(x+1, y, locations) + 1
    except IndexError:
        pass
    # TRY LEFT
    try:
        if y == 0:
            pass
        elif locations[x][y-1] not in [-1, 9]:
            locations[x][y-1] = -1
            rec_sum += traverse_rec(x, y-1, locations) + 1
    except IndexError:
        pass

    return rec_sum


def traverse(x, y, locations):
    # TRY UP
    result = 1
    locations[x][y] = -1
    try:
        if x == 0:
            pass
        elif locations[x-1][y] not in [-1, 9]:
            locations[x-1][y] = -1
            result += traverse_rec(x-1, y, locations) + 1
        else:
            pass
    except IndexError:
        pass
    # TRY RIGHT
    try:
        if locations[x][y+1] not in [-1, 9]:
            locations[x][y+1] = -1
            result += traverse_rec(x, y+1, locations) + 1
    except IndexError:
        pass
    # TRY DOWN
    try:
        if locations[x+1][y] not in [-1, 9]:
            locations[x+1][y] = -1
            result += traverse_rec(x+1, y, locations) + 1
    except IndexError:
        pass
    # TRY LEFT
    try:
        if y == 0:
            pass
        elif locations[x][y-1] not in [-1, 9]:
            locations[x][y-1] = -1
            result += traverse_rec(x, y-1, locations) + 1
    except IndexError:
        pass

    # print(x,y,result)
    return result


def get_result(arr):
    third = first = second = -math.inf

    for i in range(0, len(arr)):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] > second:
            third = second
            second = arr[i]
        elif arr[i] > third:
            third = arr[i]
    return first * second * third


def main():
    with open('input.txt', 'r') as f:
        data = f.readlines()
        locations = []
        for line in data:
            row = line.strip()
            row_numbers = [int(n) for n in row]
            locations.append(row_numbers)
        numbers = []
        for i, row in enumerate(locations):
            for j, value in enumerate(row):
                if check_neighbour(i-1, j, value, locations) and check_neighbour(i+1, j, value, locations) and check_neighbour(i, j-1, value, locations) and check_neighbour(i, j+1, value, locations):
                    numbers.append([i, j, value])

        all_values = []
        for n in numbers:
            all_values.append(traverse(n[0], n[1], locations))

        print(get_result(all_values))


if __name__ == '__main__':
    main()
