"""
*    author:  kattsun
*    created: 17-02-2021 08:45:29
"""

def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    e = 0
    ans = 0

    for i in range(n):
        e += p[i]*(p[i]+1)/2/p[i]
        if i >= k:
            e -= p[i-k]*(p[i-k]+1)/2/p[i-k]
        ans = max(ans, e)
    
    print(ans)

if __name__ == '__main__':
    main()