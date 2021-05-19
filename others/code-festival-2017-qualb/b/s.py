"""
*    author:  kattsun
*    created: 20-05-2021 07:29:50
"""


def main():
    N = int(input())
    D = list(map(int, input().split()))
    M = int(input())
    T = list(map(int, input().split()))
    d = dict()
    for i in D:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in T:
        if i in d and d[i] != 0:
            d[i] -= 1
        else:
            print('NO')
            return
    print('YES')


if __name__ == '__main__':
    main()
