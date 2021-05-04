"""
*    author:  kattsun
*    created: 03-05-2021 23:52:14
"""


def main():
    a, b, c = map(int, input().split())
    ttl = 100 * a + 10 * b + c
    if ttl % 4 == 0:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
