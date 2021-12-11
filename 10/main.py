# from functools import

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

        points = 0
        for line in data:
            string_line = line.strip()
            stash = []
            for c in string_line:
                print(stash)
                if c in opening:
                    stash.append(c)
                elif c in closing:
                    if otc[stash[-1]] != c:
                        print(f'expected: {otc[stash[-1]]}, received: {c}')
                        points += ctp[c]
                        break
                    else:
                        stash.pop()
        print(points)


if __name__ == '__main__':
    main()
