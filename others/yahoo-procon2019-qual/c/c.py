"""
*    author:  kattsun
*    created: 18-03-2021 19:52:06
"""


def main():
    k, a, b = map(int, input().split())
    ans = 1
    if a >= b - 2:
        ans += k
    else:
        ans = a
        res = k - a + 1
        ans += (b - a) * max(0, res // 2)
        if res % 2 == 1:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
