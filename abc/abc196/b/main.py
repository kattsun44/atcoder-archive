"""
*    author:  kattsun
*    created: 24-06-2021 23:52:26
"""


def main():
    N = str(input())
    if '.' in N:
        N = N[:N.find('.')]
    print(N)


if __name__ == '__main__':
    main()
