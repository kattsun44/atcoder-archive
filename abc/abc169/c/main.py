"""
*    author:  kattsun
*    created: 29-05-2021 09:51:24
"""
from math import floor
from decimal import Decimal


def main():
    a, b = input().split()
    a = int(a)
    b = Decimal(b) * 100
    print((a*b)//100)


if __name__ == '__main__':
    main()
