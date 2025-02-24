"""
*    author:  kattsun
*    created: 20-02-2021 21:15:01
"""

def main():
    n,k = map(int, input().split())
    ans = n

    for i in range(k):
        l = list(str(ans))
        g1 = int("".join(sorted(l)))
        g2 = int("".join(sorted(l,reverse=True)))
        ans = g2-g1
    
    print(ans)

if __name__ == '__main__':
    main()