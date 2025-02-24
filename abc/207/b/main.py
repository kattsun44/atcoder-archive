"""
*    author:  kattsun
*    created: 19-11-2021 20:43:09
"""


def main():
    A, B, C, D = map(int, input().split())
    if C * D - B == 0 or A / (C * D - B) < 0:
        print(-1)
    else:
        print(-(-A // (C * D - B)))


if __name__ == '__main__':
    main()
