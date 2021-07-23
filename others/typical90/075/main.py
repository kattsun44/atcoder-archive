"""
*    author:  kattsun
*    created: 23-07-2021 11:04:05
"""


def factorization(n):
    """nを素因数分解"""
    """2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def main():
    N = int(input())
    prime_factors = factorization(N)

    # 素因数の個数
    prime_factor_cnt = 0
    for prime_factor in prime_factors:
        prime_factor_cnt += prime_factor[1]

    # 素因数の個数を超えた瞬間の cnt が答え
    x = 1
    cnt = 0
    while x < prime_factor_cnt:
        x *= 2
        cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
