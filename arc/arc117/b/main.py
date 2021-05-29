"""
*    author:  kattsun
*    created: 29-05-2021 18:23:55
"""


def main():
    N = int(input())
    A = [0] + list(map(int, input().split()))
    A.sort()
    ans = 1
    for i in range(N):
        ans *= (A[i+1] - A[i] + 1)
    print(ans % 1000000007)


if __name__ == '__main__':
    main()
