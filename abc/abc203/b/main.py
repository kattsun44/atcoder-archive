"""
*    author:  kattsun
*    created: 30-05-2021 21:01:58
"""


def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(N):
        for j in range(K):
            ans += (i+1) * 100 + j + 1
    print(ans)


if __name__ == '__main__':
    main()
