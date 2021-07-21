"""
*    author:  kattsun
*    created: 19-07-2021 12:41:31
"""
def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    F = [0] * 10**6
    ans = 0
    for i in range(N-1):
        f = A[i+1] - A[i]
        F[i] = f
        ans += abs(f)
    for i in range(Q):
        L, R, V = map(int, input().split())
        L -= 1
        R -= 1
        before = abs(F[L-1]) + abs(F[R])
        if L >= 1: F[L-1] += V
        if R <= N - 2: F[R] -= V
        after = abs(F[L-1]) + abs(F[R])
        ans += after - before
        print(ans)

if __name__ == '__main__':
    main()