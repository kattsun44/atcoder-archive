"""
*    author:  kattsun
*    created: 30-05-2021 20:59:54
"""


def main():
    a, b, c = map(int, input().split())
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    else:
        print(0)


if __name__ == '__main__':
    main()
