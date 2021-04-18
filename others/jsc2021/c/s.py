"""
*    author:  kattsun
*    created: 17-04-2021 16:28:13
"""
from math import gcd, sqrt, floor


def main():
    A, B = map(int, input().split())
    ans = 0
    for c in range(1, B):
        if B // c - (A - 1) // c >= 2:
            ans = c
    print(ans)


if __name__ == '__main__':
    main()
