"""
*    author:  kattsun
*    created: 08-08-2021 20:59:27
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    sortA = sorted(A)
    print(A.index(sortA[-2])+1)


if __name__ == '__main__':
    main()
