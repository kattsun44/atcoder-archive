"""
*    author:  kattsun
*    created: 20-05-2021 07:54:52
"""


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(-(-(N-1)//(K-1)))


if __name__ == '__main__':
    main()
