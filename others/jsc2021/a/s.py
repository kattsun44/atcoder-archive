"""
*    author:  kattsun
*    created: 17-04-2021 16:10:16
"""


def main():
    x, y, z = map(int, input().split())

    print(-(-y * z // x) - 1)


if __name__ == '__main__':
    main()
