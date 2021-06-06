"""
*    author:  kattsun
*    created: 07-06-2021 08:24:56
"""

def main():
    a, b, c, x, y = map(int, input().split())
    ans = 0
    if c * 2 <= a + b:
        ans += c * 2 * min(x, y)
        if x > y:
            ans += min(a * (x-y), c * 2 * (x-y))
        elif x < y:
            ans += min(b * (y-x), c * 2 * (y-x))
    else:
        ans += a * x + b * y
    print(ans)

if __name__ == '__main__':
    main()