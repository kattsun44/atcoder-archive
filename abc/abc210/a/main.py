"""
*    author:  kattsun
*    created: 17-07-2021 20:56:25
"""

N, A, X, Y = map(int, input().split())
if A < N:
    print(A * X + (N - A) * Y)
else:
    print(N * X)
