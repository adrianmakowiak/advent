from collections import Counter

def main():
    with open('data.txt', 'r') as f:
        data = f.read()
        input, instructions = data.split('\n\n')
        print(input)
        input = input.strip()
        dict_instructions = {}
        for line in instructions.strip().split('\n'):
            i, o = line.strip().split(' -> ')
            dict_instructions[i] = o
        print(dict_instructions)

        for i in range(10):
            new_string = ''
            for j in range(len(input) - 1):
                new_string += input[j]
                print(input[j])
                key = f'{input[j]}{input[j+1]}'
                if key in dict_instructions:
                    new_string += dict_instructions[key]
            input = new_string + input[-1]
        print(len(input))
        input_counter = Counter(input).most_common()
        most = input_counter[0]
        least = input_counter[-1]
        print(most[1] - least[1])

if __name__ == '__main__':
    main()
