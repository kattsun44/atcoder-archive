"""
*    author:  kattsun
*    created: 15-05-2021 21:06:12
"""
import itertools
from math import factorial as ft


def main():
    S = input().strip()
    d = {'o': 0, 'x': 0, '?': 0}
    for c in S:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    if d['o'] >= 5:
        print(0)
    elif d['o'] == 4:
        print(ft(4))
    elif d['o'] == 3:
        print(ft(4) // 2 * 3 + ft(3) * d['?'] * 4)
    elif d['o'] == 2:
        print(14 + 6 * d['?'] * 4 + 2 * d['?'] ** 2 * 6)
    elif d['o'] == 1:
        print(1 + d['?'] * 4 + d['?'] ** 2 * 6 + d['?'] ** 3 * 4)
    else:
        print(d['?'] ** 4)


if __name__ == '__main__':
    main()
