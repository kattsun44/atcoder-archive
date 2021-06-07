"""
*    author:  kattsun
*    created: 06-06-2021 20:59:16
"""


def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - (x+y))


if __name__ == '__main__':
    main()
