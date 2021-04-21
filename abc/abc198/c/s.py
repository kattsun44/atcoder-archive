"""
*    author:  kattsun
*    created: 21-04-2021 08:15:09
"""
from math import sqrt
def main():
    R, X, Y = map(int, input().split())
    D = sqrt(X * X + Y * Y)

    if R > D and D != 0:
        print(2)
    else:
        print(int(-(-D // R)))

if __name__ == '__main__':
    main()