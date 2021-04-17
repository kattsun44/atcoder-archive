"""
*    author:  kattsun
*    created: 17-04-2021 16:15:29
"""


def main():
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    l = list((a - b) | (b - a))

    l.sort()
    l = [str(a) for a in l]

    print(' '.join(l))


if __name__ == '__main__':
    main()
