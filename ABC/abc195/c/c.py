"""
*    author:  kattsun
*    created: 13-03-2021 21:20:03
"""

def main():
    n = int(input())
    o = 1000
    ans = 0
    while n >= o:
        ans += (n//o-1)*o+1+n%o
        o = o*1000
    print(ans)

if __name__ == '__main__':
    main()