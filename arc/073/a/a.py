"""
*    author:  kattsun
*    created: 20-02-2021 08:47:54
"""

def main():
    n,t = map(int, input().split())
    T = list(map(int, input().split()))
    ans = 0

    for i in range(n-1):
        ans += min(T[i+1]-T[i],t)
    ans += t
    
    print(ans)

if __name__ == '__main__':
    main()