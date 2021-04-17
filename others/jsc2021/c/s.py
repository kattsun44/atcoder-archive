"""
*    author:  kattsun
*    created: 17-04-2021 16:28:13
"""
from math import gcd, sqrt, floor


def main():
    A, B = map(int, input().split())
    ans = 0
    for i in range(A, A + -(-(B - A) // 2)):
        for j in range(i + -(-(B - A) // 2), B + 1, i):
            ans = max(ans, gcd(i, j))
    print(ans)


if __name__ == '__main__':
    main()
