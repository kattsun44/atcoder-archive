"""
*    author:  kattsun
*    created: 17-07-2021 20:56:33
"""
from collections import deque


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    d = dict()
    for i in range(K):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    ans = len(d)
    for i in range(N - K):
        d[A[i]] -= 1
        if d[A[i]] == 0:
            d.pop(A[i])
        if A[i + K] in d:
            d[A[i + K]] += 1
        else:
            d[A[i + K]] = 1
        ans = max(ans, len(d))
    print(ans)


if __name__ == "__main__":
    main()
