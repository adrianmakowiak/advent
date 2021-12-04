def main():
    with open('data.txt', 'r') as f:
        depth = 0
        horizontal = 0
        for line in f:
            current = line.strip().split()
            cmd, value = [current[0], int(current[1])]
            if cmd == 'forward':
                horizontal += value
            elif cmd == 'up':
                depth -= value
            elif cmd == 'down':
                depth += value
        print(depth * horizontal)


if __name__ == '__main__':
    main()
