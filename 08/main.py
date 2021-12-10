# from functools import

def main():
    with open('data.txt', 'r') as f:
        data = f.readlines()
        # 1 = len(2) TR & BR
        # 4 = len(4) TR & BR & TL & M   ## BASED ON 1 WE CAN SEPARATE TL BR FROM TL M
        # 7 = len(3) T  & TR & BR       ## WE CAN FOR SURE KNOW WHICH ONE IS T
        # 8 = len(7) ALL # DOESNT HELP AT ALL

        # 0 = len(6) ALL, EXCEPT M
        # 6 = len(6) ALL, EXCEPT TR
        # 9 = len(6) ALL, EXCEPT BL
        # 2 = len(5) ALL, EXCEPT TL & BR
        # 3 = len(5) ALL, EXCEPT TL & BL
        # 5 = len(5) ALL, EXCEPT TR & BL
        """
        ALGORITHM
        GOT 1
        TR: C | F
        BR: C | F

        GOT 4 subtracting 4 from 1 gives us M AND TL
        TR: C | F
        BR: C | F
        M: B | D
        TL: B | D
        
        GOT 7 subtracting from 1 GIVES US T
        TR: C | F
        BR: C | F
        M: B | D
        TL: B | D
        T: A
        
        GOT 0, 6, 9. If we compare them to 4 and find one that has all parts of 4 it's 9
        GOT 9 Since we got already T, we can get B by subtracting T(from 7) and all parts from 4. One letter that is missing from 9 is BL
        TR: C | F
        BR: C | F
        M: B | D
        TL: B | D
        T: A
        B: G
        BL: F
        
        GOT 0, 6. If we compare them to 1, the one that has same parts as 1 is 0.
        GOT 0. The one that is missing is M. Thanks to M and TL being the same. We got TL and M at the same time
        TR: C | F
        BR: C | F
        M: D
        TL: B
        T: A
        B: G
        BL: F

        
        GOT 6, WE KNOW 0,1,4,7,8,9. 
        WE can compare 6 to 0. One that is present on 0 and not on 6 is TR. With TR we get BR
        TR: C
        BR: C
        M: D
        TL: B
        T: A
        B: G 
        BL: F
        """

        #   TTTT
        # TL    TR
        # TL    TR
        #   MMMM
        # BL    BR
        # BL    BR
        #   BBBB


        numbers_segments = {
        #     0: ['T', 'TL', 'TR', 'BL', 'BR', 'B'],
        #     1: ['TR', 'BR'],
            2: ['T', 'TR', 'M', 'BL', 'B'],
            3: ['T', 'TR', 'M', 'BR', 'B'],
            # 4: ['T', 'TL', 'TR', 'BL', 'BR', 'B'],
            5: ['T', 'TL', 'M', 'BR', 'B'],
            # 6: ['T', 'TL', 'TR', 'BL', 'BR', 'B'],
            # 7: ['T', 'TL', 'TR', 'BL', 'BR', 'B'],
            # 8: ['T', 'TL', 'TR', 'BL', 'BR', 'B'],
            # 9: ['T', 'TL', 'TR', 'BL', 'BR', 'B'],
        }
        sum = 0
        for line in data:
            segments = {
                'T': set(),
                'TL': set(),
                'TR': set(),
                'M': set(),
                'BL': set(),
                'BR': set(),
                'B': set(),
            }

            numbers = {
                0: [],
                1: None,
                2: [],
                3: [],
                4: None,
                5: [],
                6: [],
                7: None,
                8: None,
                9: [],
            }


            [input, output] = line.strip().split('|')
            input_array = input.strip().split()
            for number in input_array:
                if len(number) == 2:
                    numbers[1] = number
                elif len(number) == 4:
                    numbers[4] = number
                elif len(number) == 3:
                    numbers[7] = number
                elif len(number) == 7:
                    numbers[8] = number
                elif len(number) == 6:
                    numbers[0].append(number)
                    numbers[6].append(number)
                    numbers[9].append(number)
                elif len(number) == 5:
                    numbers[2].append(number)
                    numbers[3].append(number)
                    numbers[5].append(number)

            # STEP 1
            segments_1 = set([c for c in numbers[1]])

            segments['TR'] = segments_1
            segments['BR'] = segments_1.copy()

            # STEP 2
            segments_4 = set([c for c in numbers[4]])
            segments['TL'] = segments_4 - segments_1
            segments['M'] = segments_4 - segments_1

            # STEP 3
            segments_7 = set([c for c in numbers[7]])
            segments['T'] = segments_7 - segments_1

            # STEP 4 # 0 6 9
            candidates_array = []
            candidate = None
            candidate_string = None
            last_difference = None
            for n in numbers[0]:
                candidates_array.append(set([c for c in n]))
                difference = len(candidates_array[-1] - segments_4)
                if not candidate or (candidate and last_difference > difference):
                    candidate = candidates_array[-1]
                    candidate_string = n
                    last_difference = difference
            numbers[9] = candidate_string
            segments['B'] = (candidate - segments_4) - segments['T']

            segments_8 = set([c for c in numbers[8]])
            segments['BL'] = segments_8 - candidate

            # STEP 5 # 0, 6
            numbers[0].remove(numbers[9])
            numbers[6].remove(numbers[9])
            for n in numbers[0]:
                candidate = set([c for c in n])
                if len(candidate - segments_1) == 4:
                    numbers[0] = n
                    segments['M'] = segments_8 - candidate
                    segments['TL'] = segments['TL'] - segments['M']
                else:
                    numbers[6] = n

            # STEP 6
            segments_0 = set([c for c in numbers[0]])
            segments_6 = set([c for c in numbers[6]])
            segments['TR'] = segments_0 - segments_6
            segments['BR'] = segments['BR'] - segments['TR']

            for number in numbers[2]:
                found = False
                for segment in numbers_segments[2]:
                    (letter_to_check,) = segments[segment]
                    if letter_to_check in number:
                        found = True
                    else:
                        found = False
                        break
                if found:
                    numbers[2] = number
                    break

            for number in numbers[3]:
                found = False
                for segment in numbers_segments[3]:
                    (letter_to_check,) = segments[segment]
                    if letter_to_check in number:
                        found = True
                    else:
                        found = False
                        break
                if found:
                    numbers[3] = number
                    break

            for number in numbers[5]:
                found = False
                for segment in numbers_segments[5]:
                    (letter_to_check,) = segments[segment]
                    if letter_to_check in number:
                        found = True
                    else:
                        found = False
                        break
                if found:
                    numbers[5] = number
                    break

            numbers = {value:key for (key, value) in numbers.items()}
            print(numbers)
            output_array = output.strip().split()
            print(output_array)
            # print(o1, o2, o3, o4)
            number_string = ''
            for signal in output_array:
                for key, value in numbers.items():
                    if len(signal) != len(key):
                        continue
                    found = False
                    for letter in signal:
                        if letter in key:
                            found = True
                        else:
                            found = False
                            break
                    if found:
                        number_string += str(value)
                        break
            print(number_string)
            sum += int(number_string)
            print('\n')
        print(sum)
            # print(f'Input: {input} output: {output}')


if __name__ == '__main__':
    main()
