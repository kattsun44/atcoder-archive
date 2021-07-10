"""
*    author:  kattsun
*    created: 10-07-2021 10:43:34
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 0
    for i in range(N):
        ans += abs(A[i]-B[i])
    print(ans)


if __name__ == '__main__':
    main()
