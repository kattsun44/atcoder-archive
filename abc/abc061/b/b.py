"""
*    author:  kattsun
*    created: 10-04-2021 22:37:13
"""


def main():
    N, M = map(int, input().split())
    L = list(range(1, N + 1))
    cnt = dict(zip(L, [0] * N))

    for i in range(M):
        a, b = map(int, input().split())
        cnt[a] += 1
        cnt[b] += 1

    for i in range(N):
        print(cnt[i+1])


if __name__ == '__main__':
    main()
