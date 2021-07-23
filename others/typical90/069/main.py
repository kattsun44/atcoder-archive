"""
*    author:  kattsun
*    created: 22-07-2021 19:28:30
"""


def binpow(a, b, mod):
    ans = 1
    while b != 0:
        if b % 2 == 1:  # 末尾のビットが1のときに値を更新
            ans = ans * a % mod
        a = a * a % mod  # 繰り返し2乗していく
        b //= 2  # b = b >> 1 と同じ、つまり1ビット右へシフト
    return ans


def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    if N == 1:
        print(K % mod)
    elif N == 2:
        print(K * (K-1) % mod)
    else:
        ans = K * (K-1) % mod
        ans = ans * binpow(K-2, N-2, mod) % mod
        print(ans)


if __name__ == '__main__':
    main()
