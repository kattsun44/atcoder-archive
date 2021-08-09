"""
*    author:  kattsun
*    created: 09-08-2021 08:09:40
"""
from bisect import bisect_left


def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    valsA = sorted(set(A))
    valsB = sorted(set(B))
    for i in range(N):
        x = bisect_left(valsA, A[i])+1
        y = bisect_left(valsB, B[i])+1
        print(x, y)


if __name__ == '__main__':
    main()
