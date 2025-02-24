"""
*    author:  kattsun
*    created: 04-04-2021 21:55:20
"""


def main():
    a, b, c = map(int, input().split())

    print(min(a+b, a+c, b+c))


if __name__ == '__main__':
    main()
