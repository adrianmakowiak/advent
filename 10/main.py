# from functools import
import math


def main():
    with open('data.txt', 'r') as f:
        data = f.readlines()
        opening = ['(', '[', '{', '<']
        closing = [')', ']', '}', '>']
        otc = {
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>',
        }
        ctp = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137,
        }

        otp = {
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4,
        }

        points = 0
        scores = []
        for line in data:
            string_line = line.strip()
            stash = []
            broken = False
            for c in string_line:
                if c in opening:
                    stash.append(c)
                elif c in closing:
                    if otc[stash[-1]] != c:
                        # print(f'expected: {otc[stash[-1]]}, received: {c}')
                        points += ctp[c]
                        broken = True
                        break
                    else:
                        stash.pop()
            if not broken:
                score = 0
                for p in reversed(stash):
                    score = score * 5 + otp[p]
                scores.append(score)
        print(sorted(scores)[math.floor(len(scores)/2)])


if __name__ == '__main__':
    main()
