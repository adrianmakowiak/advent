def main():
    with open('data.txt', 'r') as f:
        values = f.readlines()
        values_copy = values.copy()
        dominating_bit_counter, ones, zeros = 0, [], []
        for index in range(len(values[0].strip())):
            for val in values:
                dominating_bit_counter = dominating_bit_counter + 1 if val[index] == "1" else dominating_bit_counter - 1
                if val[index] == '1':
                    ones.append(val)
                else:
                    zeros.append(val)
            values = ones if dominating_bit_counter >= 0 else zeros
            dominating_bit_counter, ones, zeros = 0, [], []

        oxygen = int(values[0].strip(), 2)

        dominating_bit_counter, ones, zeros = 0, [], []
        for index in range(len(values_copy[0].strip())):
            for val in values_copy:
                dominating_bit_counter = dominating_bit_counter + 1 if val[index] == "1" else dominating_bit_counter - 1
                if val[index] == '1':
                    ones.append(val)
                else:
                    zeros.append(val)
            values_copy = zeros if dominating_bit_counter >= 0 else ones
            if len(values_copy) == 1:
                break
            dominating_bit_counter, ones, zeros = 0, [], []

        co2 = int(values_copy[0].strip(), 2)

        print(oxygen * co2)


if __name__ == '__main__':
    main()
