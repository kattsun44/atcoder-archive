"""
*    author:  kattsun
*    created: 01-07-2021 08:40:36
"""
from math import gcd


def main():
    A, B, C = map(int, input().split())
    GCD = gcd(A, gcd(B, C))
    print((A+B+C)//GCD-3)


if __name__ == '__main__':
    main()
