"""
*    author:  kattsun
*    created: 18-04-2021 15:55:34
"""


def main():
    N, P = map(int, input().split())
    MOD = 1000000007
    ans = (P - 1) * pow(P - 2, N - 1, MOD) % MOD
    print(ans)


if __name__ == '__main__':
    main()
