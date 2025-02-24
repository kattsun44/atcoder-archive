"""
*    author:  kattsun
*    created: 17-04-2021 10:09:56
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ttl = 0
    a_sum = 0
    div = 10 ** 9 + 7

    for i in range(N - 1):
        a_sum += A[i]
        ttl += a_sum * A[i + 1]

    print(ttl % div)


if __name__ == '__main__':
    main()
