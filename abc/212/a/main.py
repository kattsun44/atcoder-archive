"""
*    author:  kattsun
*    created: 31-07-2021 20:52:57
"""


def main():
    A, B = map(int, input().split())
    if A > 0 and B > 0:
        print('Alloy')
    elif A != 0:
        print('Gold')
    else:
        print('Silver')


if __name__ == '__main__':
    main()
