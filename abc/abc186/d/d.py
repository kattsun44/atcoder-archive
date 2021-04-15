"""
*    author:  kattsun
*    created: 15-04-2021 09:13:36
"""

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0

    for i in range(N):
        # i番目の数に i * 2 - (N-1) をかけた数の累積が答え
        ans += A[i] * (i*2 - N + 1)
    
    print(ans)

if __name__ == '__main__':
    main()