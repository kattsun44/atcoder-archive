"""
*    author:  kattsun
*    created: 31-07-2021 20:57:03
"""


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sa = set(A)
    sb = set(B)

    C = []
    for i in range(N):
        C.append((A[i], 'a'))
    for i in range(M):
        C.append((B[i], 'b'))
    C_sorted = sorted(C, key=lambda x: x[0])

    D = []
    for i in range(len(C)-1):
        if C_sorted[i+1][1] != C_sorted[i][1]:
            D.append(C_sorted[i+1][0]-C_sorted[i][0])
    print(min(D))


if __name__ == '__main__':
    main()
