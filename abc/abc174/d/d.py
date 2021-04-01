"""
*    author:  kattsun
*    created: 16-02-2021 21:02:38
"""

def main():
    n = int(input())
    s = input().strip()
    ans = n

    ls = 0
    rs = s.count('R')

    for i in range(n+1):
        ans = min(ans, max(ls, rs))
        if i != n:
            ls += s[i].count('W')
            rs -= s[i].count('R')
    
    print(ans)


if __name__ == '__main__':
    main()