"""
*    author:  kattsun
*    created: 07-05-2021 08:26:17
"""
from math import sqrt, floor
from decimal import Decimal

def main():
    N = int(input())
    a = str(N * 8 + 9)
    x = floor((-1 + Decimal(a)**Decimal('0.5')) / 2)
    print(N - x + 1)

if __name__ == '__main__':
    main()