"""
*    author:  kattsun
*    created: 09-05-2021 09:46:05
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    bucket = [0] * 202
    ans = 0

    for i in range(N):
        mo = A[i] % 200
        ans += bucket[mo]
        bucket[mo] += 1

    print(ans)


if __name__ == '__main__':
    main()
