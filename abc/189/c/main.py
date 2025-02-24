"""
*    author:  kattsun
*    created: 30-05-2021 10:21:09
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for l in range(N):
        x_min = A[l]
        for r in range(l, N):
            x_min = min(x_min, A[r])
            ans = max(ans, x_min * (r-l+1))
    print(ans)


if __name__ == '__main__':
    main()
