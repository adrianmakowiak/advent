from statistics import mean, median
import numpy as np
import math


def main():
    with open('data.txt', 'r') as f:
        data = f.readline()
        crabs_position = [int(pos) for pos in data.strip().split(',')]
        average = round(mean(crabs_position))
        result_median = int(median(crabs_position))
        last_result = math.inf

        for value in range(average, result_median, -1):
            fuel_used = 0
            for pos in crabs_position:
                steps = abs(value - pos)
                for i in range(steps):
                    fuel_used += i + 1
            if last_result < fuel_used:
                print(last_result)
                return
            else:
                last_result = fuel_used


if __name__ == '__main__':
    main()
