from collections import Counter
import operator

def main():
    with open('data.txt', 'r') as f:
        data = f.read()
        input, instructions = data.split('\n\n')
        print(input)
        input = input.strip()
        pairs = {}
        singles = {}
        dict_instructions = {}
        for line in instructions.strip().split('\n'):
            i, o = line.strip().split(' -> ')
            dict_instructions[i] = o
        print(dict_instructions)

        for i in range(len(input) - 1):
            pair = f'{input[i]}{input[i+1]}'
            if pair in pairs:
                pairs[pair] += 1
            else:
                pairs[pair] = 1

            if input[i] in singles:
                singles[input[i]] += 1
            else:
                singles[input[i]] = 1

        if input[-1] in singles:
            singles[input[-1]] += 1
        else:
            singles[input[-1]] = 1
        print(pairs)
        print(singles)
        # NBCCNBBBCBHCB
        for i in range(40):
            new_pairs = {}
            new_singles = {}
            for key, value in pairs.items():
                if key in dict_instructions:
                    key1 = f'{key[0]}{dict_instructions[key]}'
                    key2 = f'{dict_instructions[key]}{key[1]}'
                    if key1 in new_pairs:
                        new_pairs[key1] += value
                    else:
                        new_pairs[key1] = value

                    if key2 in new_pairs:
                        new_pairs[key2] += value
                    else:
                        new_pairs[key2] = value


            #         if key[0] in new_singles:
            #             new_singles[key[0]] += value
            #         else:
            #             new_singles[key[0]] = value
            #
            #         if key[1] in new_singles:
            #             new_singles[key[1]] += value
            #         else:
            #             new_singles[key[1]] = value
            #
                    if dict_instructions[key] in singles:
                        singles[dict_instructions[key]] += value
                    else:
                        singles[dict_instructions[key]] = value
            pairs = new_pairs
            # singles = new_singles
        print(pairs)
        print(singles)
        # singles_counter = Counter(singles.values()).most_common()
        maxi = max(singles.items(), key=operator.itemgetter(1))[1]
        mini = min(singles.items(), key=operator.itemgetter(1))[1]
        print(maxi - mini)


if __name__ == '__main__':
    main()
