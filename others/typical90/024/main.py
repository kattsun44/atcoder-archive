"""
*    author:  kattsun
*    created: 03-07-2021 16:17:32
"""


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    diff = 0
    for i in range(N):
        diff += abs(A[i]-B[i])
    if K < diff:
        print('No')
    elif K % 2 == 0 and diff % 2 == 0 or K % 2 == 1 and diff % 2 == 1:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
