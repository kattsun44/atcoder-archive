"""
*    author:  kattsun
*    created: 03-04-2021 20:37:10
"""


def main():
    a, b, c, k = map(int, input().split())

    if k % 2 == 0:
        print(a - b)
    else:
        print(b-a)


if __name__ == '__main__':
    main()
