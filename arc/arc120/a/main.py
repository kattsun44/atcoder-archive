"""
*    author:  kattsun
*    created: 16-06-2021 10:49:10
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    maxA = 0
    pre_accum = 0
    accum = 0
    for i in range(N):
        maxA = max(maxA, A[i])
        pre_accum += accum
        accum += A[i]
        print(pre_accum + accum + maxA*(i+1))


if __name__ == '__main__':
    main()
