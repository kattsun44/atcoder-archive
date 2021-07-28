"""
*    author:  kattsun
*    created: 28-07-2021 08:02:20
"""
def change_min(dp, i, x):
    if dp[i] > x:
        dp[i] = x
        return True
    return False

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    inf = float('inf')
    dp = [0] + [inf] * (N-1)
    for i in range(1, N):
        for j in range(K+1):
            if i > j - 1:
                change_min(dp, i, dp[i-j] + abs(h[i] - h[i - j]))
    print(dp[-1])

if __name__ == '__main__':
    main()