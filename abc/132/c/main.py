"""
*    author:  kattsun
*    created: 16-08-2021 20:44:57
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    halfA1 = A[:N//2]
    halfA2 = A[N//2:]
    print(halfA2[0] - halfA1[-1])


if __name__ == '__main__':
    main()
