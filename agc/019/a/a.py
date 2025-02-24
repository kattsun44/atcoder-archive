"""
*    author:  kattsun
*    created: 20-02-2021 07:34:59
"""

def main():
    q,h,s,d = map(int, input().split())
    n = int(input())

    ans = int(n/2) * min(q*8,h*4,s*2,d) + n % 2 * min(q*4,h*2,s)
    print(ans)


if __name__ == '__main__':
    main()