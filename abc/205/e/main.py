"""
*    author:  kattsun
*    created: 13-06-2021 22:28:39
"""
from operator import mul
from functools import reduce


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


def main():
    N, M, K = map(int, input().split())
    n = 1000000007
    if N > M + K:
        print(0)
    elif N == M+K:
        print(2**(N+M-1) % n)
    elif N <= K:
        print(2**(N+M) % n)
    else:
        print((combinations_count(N+M, N)-combinations_count(N+M-(K+1), M)) % n)


if __name__ == '__main__':
    main()
