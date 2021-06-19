"""
*    author:  kattsun
*    created: 19-06-2021 10:02:16
"""


def main():
    N = int(input())

    def get_index(x):
        i = 1 if x >= N else 0
        return x//N, x % N

    S = input().strip()
    S1 = list(S[:N])
    S2 = list(S[N:])
    L = [S1, S2]

    Q = int(input())
    for i in range(Q):
        T, A, B = map(int, input().split())
        A -= 1
        B -= 1
        if T == 1:
            a1, a2 = get_index(A)
            b1, b2 = get_index(B)
            L[a1][a2], L[b1][b2] = L[b1][b2], L[a1][a2]
        else:
            L[0], L[1] = L[1], L[0]
    print(''.join(L[0]) + ''.join(L[1]))


if __name__ == '__main__':
    main()
