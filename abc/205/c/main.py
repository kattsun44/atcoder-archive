"""
*    author:  kattsun
*    created: 13-06-2021 21:04:36
"""


def main():
    A, B, C = map(int, input().split())
    diff = 0
    if C % 2 == 0:
        diff = abs(A) - abs(B)
    else:
        diff = A - B

    if diff > 0:
        print('>')
    elif diff == 0:
        print('=')
    else:
        print('<')


if __name__ == '__main__':
    main()
