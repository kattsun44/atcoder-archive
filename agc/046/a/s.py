"""
*    author:  kattsun
*    created: 25-04-2021 13:33:59
"""


def main():
    X = int(input())
    for k in range(1, 361):
        if k * X % 360 == 0:
            print(k)
            return


if __name__ == '__main__':
    main()
