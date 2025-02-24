"""
*    author:  kattsun
*    created: 14-08-2021 23:38:24
"""


def main():
    A, B = map(int, input().split())
    print((A+B) % 24)


if __name__ == '__main__':
    main()
