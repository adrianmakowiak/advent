# from functools import
import math


def count_flashes(matrix):
    flashes_in_step = 0
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if matrix[i][j]['flashed']:
                matrix[i][j]['flashed'] = False
                flashes_in_step += 1
                matrix[i][j]['level'] = 0
    return flashes_in_step


def increase_by_one(matrix):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            matrix[i][j]['level'] += 1


def flash(matrix) -> int:
    flashes = 0
    for i, row in enumerate(matrix):
        for j, octopus in enumerate(row):
            if octopus['level'] > 9 and not octopus['flashed']:
                matrix[i][j]['flashed'] = True
                flashes += affect_neighbours(i, j, matrix)


def affect_neighbours(x, y, matrix) -> int:
    rec_sum = 0
    # TRY UP
    try:
        if x == 0:
            pass
        elif matrix[x-1][y]:
            matrix[x-1][y]['level'] += 1
            if matrix[x-1][y]['level'] > 9 and not matrix[x-1][y]['flashed']:
                matrix[x-1][y]['flashed'] = True
                rec_sum += affect_neighbours(x-1, y, matrix) + 1
    except IndexError:
        pass
    # TRY RIGHT
    try:
        if matrix[x][y+1]:
            matrix[x][y+1]['level'] += 1
            if matrix[x][y+1]['level'] > 9 and not matrix[x][y+1]['flashed']:
                matrix[x][y+1]['flashed'] = True
                rec_sum += affect_neighbours(x, y+1, matrix) + 1
    except IndexError:
        pass
    # TRY DOWN
    try:
        if matrix[x+1][y]:
            matrix[x+1][y]['level'] += 1
            if matrix[x+1][y]['level'] > 9 and not matrix[x+1][y]['flashed']:
                matrix[x+1][y]['flashed'] = True
                rec_sum += affect_neighbours(x+1, y, matrix) + 1
    except IndexError:
        pass
    # TRY LEFT
    try:
        if y == 0:
            pass
        elif matrix[x][y-1]:
            matrix[x][y-1]['level'] += 1
            if matrix[x][y-1]['level'] > 9 and not matrix[x][y-1]['flashed']:
                matrix[x][y-1]['flashed'] = True
                rec_sum += affect_neighbours(x, y-1, matrix) + 1
    except IndexError:
        pass
    # TRY TOP-LEFT
    try:
        if x == 0 or y == 0:
            pass
        elif matrix[x-1][y-1]:
            matrix[x-1][y-1]['level'] += 1
            if matrix[x-1][y-1]['level'] > 9 and not matrix[x-1][y-1]['flashed']:
                matrix[x-1][y-1]['flashed'] = True
                rec_sum += affect_neighbours(x-1, y-1, matrix) + 1
    except IndexError:
        pass
    # TRY TOP-RIGHT
    try:
        if x == 0:
            pass
        elif matrix[x-1][y+1]:
            matrix[x-1][y+1]['level'] += 1
            if matrix[x-1][y+1]['level'] > 9 and not matrix[x-1][y+1]['flashed']:
                matrix[x-1][y+1]['flashed'] = True
                rec_sum += affect_neighbours(x-1, y+1, matrix) + 1
    except IndexError:
        pass
    # TRY BOTTOM-RIGHT
    try:
        if matrix[x+1][y+1]:
            matrix[x+1][y+1]['level'] += 1
            if matrix[x+1][y+1]['level'] > 9 and not matrix[x+1][y+1]['flashed']:
                matrix[x+1][y+1]['flashed'] = True
                rec_sum += affect_neighbours(x+1, y+1, matrix) + 1
    except IndexError:
        pass

    # TRY BOTTOM-LEFT
    try:
        if y == 0:
            pass
        elif matrix[x+1][y-1]:
            matrix[x+1][y-1]['level'] += 1
            if matrix[x+1][y-1]['level'] > 9 and not matrix[x+1][y-1]['flashed']:
                matrix[x+1][y-1]['flashed'] = True
                rec_sum += affect_neighbours(x+1, y-1, matrix) + 1
    except IndexError:
        pass

    return rec_sum


def main():
    with open('data.txt', 'r') as f:
        data = f.readlines()
        matrix = []
        for line in data:
            row = line.strip()
            row_numbers = [{'level': int(n), 'flashed': False} for n in row]
            matrix.append(row_numbers)
        flash_counter = 0
        while True:
            increase_by_one(matrix)
            flash(matrix)
            flash_counter += count_flashes(matrix)
            for row in matrix:
                string = ''
                for value in row:
                    string += str(value['level'])
                print(f'{string}\n')
        print(flash_counter)


if __name__ == '__main__':
    main()
