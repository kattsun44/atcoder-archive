"""
*    author:  kattsun
*    created: 13-06-2021 21:01:49
"""


def main():
    N = int(input())
    l = [i for i in range(1, N+1)]
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if A[i] != l[i]:
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    main()
