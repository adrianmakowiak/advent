def main():
    with open('data.txt', 'r') as f:
        depth, horizontal, aim = 0, 0, 0
        for line in f:
            current = line.strip().split()
            cmd, value = [current[0], int(current[1])]
            if cmd == 'forward':
                horizontal += value
                depth += aim * value
            elif cmd == 'up':
                aim -= value
            elif cmd == 'down':
                aim += value
        print(depth * horizontal)


if __name__ == '__main__':
    main()
