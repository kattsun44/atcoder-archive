"""
*    author:  kattsun
*    created: 12-08-2021 18:37:29
"""
from math import floor


def main():
    N = int(input())
    for i in range(1, N+1):
        num = floor(i * 108/100)
        if num == N:
            print(i)
            return
    print(':(')


if __name__ == '__main__':
    main()
