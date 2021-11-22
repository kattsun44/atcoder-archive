"""
*    author:  kattsun
*    created: 22-11-2021 23:54:18
"""
import math


def main():
    N = float(input())
    X = math.floor(N)
    Y = int((N - X)*10)

    if Y <= 2:
        print(str(X) + "-")
    elif Y <= 6:
        print(str(X))
    else:
        print(str(X) + "+")


if __name__ == '__main__':
    main()
