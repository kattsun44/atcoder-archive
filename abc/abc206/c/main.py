"""
*    author:  kattsun
*    created: 19-06-2021 21:04:55
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = dict()
    for i in range(N):
        if A[i] in cnt:
            cnt[A[i]] += 1
        else:
            cnt[A[i]] = 1
    ans = 0
    n = N - 1
    for i in range(N):
        ans += n
        ans -= cnt[A[i]] - 1
        cnt[A[i]] -= 1
        n -= 1
    print(ans)


if __name__ == '__main__':
    main()
