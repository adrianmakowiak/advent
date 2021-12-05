def main():
    with open('data.txt', 'r') as f:
        values = f.readlines()
        most_common = [0] * (len(values[0]) - 1)
        for val in values:
            v = val.strip()
            for i, single_bit in enumerate(v):
                most_common[i] = most_common[i] + 1 if single_bit == "1" else most_common[i] - 1

        gamma_bin = ["1" if x > 0 else "0" for x in most_common]
        epsilon_bin = ["0" if x > 0 else "1" for x in most_common]

        gamma = int(''.join(gamma_bin), 2)
        epsilon = int(''.join(epsilon_bin), 2)
        print(gamma * epsilon)


if __name__ == '__main__':
    main()
