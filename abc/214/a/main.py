"""
*    author:  kattsun
*    created: 16-11-2021 22:05:03
"""


def main():
    N = int(input())
    if N <= 125:
        print(4)
    elif N <= 211:
        print(6)
    else:
        print(8)


if __name__ == '__main__':
    main()
