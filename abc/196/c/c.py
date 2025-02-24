"""
*    author:  kattsun
*    created: 31-03-2021 19:22:09
"""


def main():
    n = int(input())
    for i in range(1, 1000001):
        s = str(i)
        if int(s * 2) > n:
            print(i - 1)
            return


if __name__ == '__main__':
    main()
