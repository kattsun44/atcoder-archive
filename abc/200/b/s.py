"""
*    author:  kattsun
*    created: 08-05-2021 21:02:57
"""


def main():
    N, K = map(int, input().split())
    for i in range(K):
        if N % 200 == 0:
            N = int(N / 200)
        else:
            N = N * 1000 + 200
    print(N)


if __name__ == '__main__':
    main()
