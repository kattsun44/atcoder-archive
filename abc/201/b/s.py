"""
*    author:  kattsun
*    created: 15-05-2021 21:02:44
"""


def main():
    N = int(input())
    d = dict()
    for i in range(N):
        S, T = map(str, input().split())
        T = int(T)
        if S not in d:
            d[S] = T
    d_sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(d_sorted[1][0])


if __name__ == '__main__':
    main()
