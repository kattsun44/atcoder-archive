"""
*    author:  kattsun
*    created: 30-07-2021 08:39:27
"""

def main():
    L, R = map(int, input().split())
    div = 10**9+7

    # Lの位に等しくなるまでxを初期化
    x = 1
    while x*10 < L:
        x *= 10

    ans = 0
    L1 = L
    R1 = min(x*10-1, R)
    while x <= R:

        # 答えを図示したときの図形
        rectangle = (L1 * (R1 - L1 + 1)) % div
        tryangle = int((R1 - L1) * (R1 - L1 + 1) / 2) % div

        ans += (rectangle + tryangle) * len(str(x))
        ans %= div
        x *= 10
        L1 = x
        R1 = min(x*10-1, R)
    print(ans)

if __name__ == '__main__':
    main()