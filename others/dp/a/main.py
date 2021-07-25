"""
*    author:  kattsun
*    created: 26-07-2021 07:22:05
"""
def change_min(dp, i, x):
    if dp[i] > x:
        dp[i] = x
        return True
    return False

def main():
    N = int(input())
    h = list(map(int, input().split()))
    inf = float('inf')
    dp = [0] + [inf] * (N-1)
    for i in range(1,N):
        change_min(dp, i, dp[i-1] + abs(h[i] - h[i-1]))
        if i > 1:
            change_min(dp, i, dp[i-2] + abs(h[i] - h[i-2]))
    print(dp[N-1])


if __name__ == '__main__':
    main()