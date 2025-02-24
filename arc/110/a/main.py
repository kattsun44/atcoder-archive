"""
*    author:  kattsun
*    created: 24-06-2021 23:36:53
"""
import math
from functools import reduce


def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)


def main():
    N = int(input())
    ans = my_lcm(*[i for i in range(2, N+1)]) + 1
    print(ans)


if __name__ == '__main__':
    main()
