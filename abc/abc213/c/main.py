"""
*    author:  kattsun
*    created: 08-08-2021 20:59:33
"""
from scipy.stats import rankdata


def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    rankA = rankdata(A, method='dense').astype(int)
    rankB = rankdata(B, method='dense').astype(int)
    for i in range(N):
        print(rankA[i], rankB[i])


if __name__ == '__main__':
    main()
