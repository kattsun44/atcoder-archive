"""
*    author:  kattsun
*    created: 30-07-2021 10:06:34
"""

def main():
    S = list(map(str, input().split()))
    ans = ''
    for c in S:
        ans += c.upper()[0]
    print(ans)

if __name__ == '__main__':
    main()