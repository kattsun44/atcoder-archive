"""
*    author:  kattsun
*    created: 13-08-2021 21:45:51
"""


def main():
    A, B = map(int, input().split())
    if A == 1:
        A += 13
    if B == 1:
        B += 13
    if A > B:
        print('Alice')
    elif A < B:
        print('Bob')
    else:
        print('Draw')


if __name__ == '__main__':
    main()
