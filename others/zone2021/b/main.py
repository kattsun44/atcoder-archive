"""
*    author:  kattsun
*    created: 10-06-2021 22:31:53
"""


def main():
    N, D, H = map(int, input().split())
    ans = 0.0
    diff = []
    for i in range(N):
        d, h = (list(map(int, input().split())))
        ans = max(ans, h - d*(H-h)/(D-d))
    print(ans)


if __name__ == '__main__':
    main()
