"""
*    author:  kattsun
*    created: 25-03-2021 23:40:24
"""


def main():
    a, b = map(int, input().split())
    if a % 3 == 0 or b % 3 == 0 or (a + b) % 3 == 0:
        print('Possible')
    else:
        print('Impossible')


if __name__ == '__main__':
    main()
