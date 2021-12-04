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


if __name__ == '__main__':
    main()

