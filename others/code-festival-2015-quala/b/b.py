"""
*    author:  kattsun
*    created: 14-02-2021 22:31:36
"""

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    
    for i in range(n):
        ans += a[i] * (2 ** (n-i-1))
    print(ans)

if __name__ == '__main__':
    main()