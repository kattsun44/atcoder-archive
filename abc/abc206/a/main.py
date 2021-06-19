"""
*    author:  kattsun
*    created: 19-06-2021 20:57:08
"""
import math


def main():
    N = int(input())
    n = math.floor(N * 1.08)
    if n < 206:
        print('Yay!')
    elif n == 206:
        print('so-so')
    else:
        print(':(')


if __name__ == '__main__':
    main()
