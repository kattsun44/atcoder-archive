"""
*    author:  kattsun
*    created: 24-06-2021 23:57:55
"""


def main():
    a, b, c, d = map(int, input().split())
    print(max(a*b, c*d))


if __name__ == '__main__':
    main()
