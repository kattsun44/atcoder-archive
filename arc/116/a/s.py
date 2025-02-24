"""
*    author:  kattsun
*    created: 04-05-2021 12:26:11
"""


def main():
    N = int(input())
    for i in range(N):
        c = int(input())
        if c % 4 == 0:
            print('Even')
        elif c % 2 == 0:
            print('Same')
        else:
            print('Odd')


if __name__ == '__main__':
    main()
