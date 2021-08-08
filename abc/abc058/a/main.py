"""
*    author:  kattsun
*    created: 07-08-2021 23:42:40
"""


def main():
    a, b, c = map(int, input().split())
    if b-a == c-b:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
