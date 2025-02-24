"""
*    author:  kattsun
*    created: 26-04-2021 08:07:25
"""
from math import gcd
from functools import reduce
def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = max(A)
    m = min(A)

    print(reduce(gcd, A))

if __name__ == '__main__':
    main()