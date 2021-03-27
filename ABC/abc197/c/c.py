"""
*    author:  kattsun
*    created: 27-03-2021 21:59:11
"""
import itertools


def OR(*args):
    a = args
    if len(a) == 2:
        return a[0] | a[1]
    return a[0] | OR(a[1:])


def main():
    n = int(input())
    a = list(map(int, input().split()))
    # print(list(itertools.combinations(a)))

    print(OR(1, 2, 3, 4))


if __name__ == '__main__':
    main()
