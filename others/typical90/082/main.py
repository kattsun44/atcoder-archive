"""
*    author:  kattsun
*    created: 30-07-2021 08:39:27
"""


def main():
    L, R = map(int, input().split())
    MOD = 10**9+7
    ans = 0
    for digit in range(1, 20):
        # 今の桁での最小・最大値
        low = 10**(digit - 1)
        high = 10**digit - 1

        l = max(L, low)
        r = min(R, high)

        if l <= r:
            # 高さl+r、幅r-l+1の長方形の面積を求め、2で割る
            ans += (l+r) * (r-l+1) * digit // 2
    
    print(ans % MOD)


if __name__ == '__main__':
    main()