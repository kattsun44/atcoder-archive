"""
*    author:  kattsun
*    created: 18-07-2021 14:53:57
"""
from operator import mul
from functools import reduce


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


def main():
    N, L = map(int, input().split())
    div = 10**9+7
    ans = 0
    step = 0
    i = 0
    while (N-step+i >= i):
        step = L * i
        ans += combinations_count(N-step+i, i)
        ans %= div
        i += 1
    print(ans-1)


if __name__ == '__main__':
    main()
