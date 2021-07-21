"""
*    author:  kattsun
*    created: 19-07-2021 07:49:35
"""

def main():
    N = int(input())
    ans = 1
    div = 10**9+7
    for i in range(N):
        A = list(map(int, input().split()))
        ans *= sum(A)
        ans %= div
    print(ans)

if __name__ == '__main__':
    main()