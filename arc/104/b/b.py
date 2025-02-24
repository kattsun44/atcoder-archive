"""
*    author:  kattsun
*    created: 10-02-2021 08:19:59
"""

def main():
    n,s = input().split()
    n = int(n)
    s = s.strip()
    ans = 0
    for i in range(n):
        c1 = 0
        c2 = 0
        for c in s[i:]:
            if c == 'A':
                c1 += 1
            elif c == 'T':
                c1 -= 1
            elif c == 'C':
                c2 += 1
            else:
                c2 -= 1
            if c1 == 0 and c2 == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()