"""
*    author:  kattsun
*    created: 05-05-2021 09:29:28
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = A[0]
    out = 0

    for i in range(N):
        a = max(a, A[i])
        b = B[i]
        out = max(out, a * b)
        print(out)


if __name__ == '__main__':
    main()
