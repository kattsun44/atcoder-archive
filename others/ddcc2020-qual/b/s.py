"""
*    author:  kattsun
*    created: 13-05-2021 08:05:53
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    a = 0
    b = sum(A)
    ans = 2020202020
    for i in range(N):
        a += A[i]
        b -= A[i]
        diff = abs(a - b)
        ans = min(diff, ans)
    print(ans)


if __name__ == '__main__':
    main()
