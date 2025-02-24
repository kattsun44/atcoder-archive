"""
*    author:  kattsun
*    created: 27-02-2021 21:22:03
"""
from math import sqrt
def main():
    n = int(input())
    ans = n
    cnt = 0
    s = set()

    for i in range(int(sqrt(n))):
        n0 = n
        e = 2
        while n0 > (i+2)**2-1:
            n0 = n0 // (i+2)
            if (i+2) ** e not in s:
                s.add((i+2)**e)
                cnt += 1
            e += 1
        ans = ans - cnt
        cnt = - 0
    
    print(ans)

if __name__ == '__main__':
    main()