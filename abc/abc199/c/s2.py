"""
*    author:  kattsun
*    created: 24-04-2021 21:08:24
"""


def main():
    N = int(input())
    S = input().strip()
    Q = int(input())
    for i in range(Q):
        T, A, B = map(int, input().split())
        A -= 1
        B -= 1
        if T == 1:
            S = S.translate(S.maketrans({S[A]: S[B], S[B]: S[A]}))
        if T == 2:
            S = S[N:] + S[:N]

    print(S)


if __name__ == '__main__':
    main()
