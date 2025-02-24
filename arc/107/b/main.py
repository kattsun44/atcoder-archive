"""
*    author:  kattsun
*    created: 11-06-2021 06:58:56
"""

def main():
    N, K = map(int, input().split())
    ans = 0
    K = abs(K)
    num = [0] * (N*2+1)
    for x in range(2, 2*(N+1)-1):
        num[x] = min(x - 1, 2*N+1-x)
    for x in range(K, 2*(N+1)-1):
        ans += num[x] * num[x-K]
    print(ans)

if __name__ == '__main__':
    main()