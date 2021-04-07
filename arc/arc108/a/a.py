"""
*    author:  kattsun
*    created: 07-04-2021 20:25:16
"""
from functools import reduce


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1] + [1]


def main():
    S, P = map(int, input().split())
    divList = make_divisors(P)
    print(divList)

    for i in range(len(divList) - 1):
        # 総乗
        print(divList[:i + 1], divList[i + 1:])
        N = reduce(lambda x, y: x * y, divList[:i + 1])
        M = reduce(lambda x, y: x * y, divList[i + 1:])
        if N + M == S and N * M == P:
            print('Yes')
            return
    print('No')
    return


if __name__ == '__main__':
    main()
