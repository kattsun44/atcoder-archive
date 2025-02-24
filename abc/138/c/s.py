"""
*    author:  kattsun
*    created: 27-04-2021 22:34:55
"""


def main():
    N = int(input())
    V = list(map(int, input().split()))
    V.sort()
    v = V[0]
    for i in range(1, N):
        v = (v + V[i]) / 2
    print(v)


if __name__ == '__main__':
    main()
