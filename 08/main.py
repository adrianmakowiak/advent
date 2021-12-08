def main():
    with open('data.txt', 'r') as f:
        data = f.readlines()
        counter = 0
        lengths = [2, 4, 3, 7]
        for line in data:
            [input, output] = line.strip().split('|')
            output_array = output.strip().split()
            # print(o1, o2, o3, o4)
            for signal in output_array:
                if len(signal) in lengths:
                    print(f'Signal: {signal}: len: {len(signal)}')
                    counter += 1
            print('\n')
        print(counter)
            # print(f'Input: {input} output: {output}')


if __name__ == '__main__':
    main()
