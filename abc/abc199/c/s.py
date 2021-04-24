"""
*    author:  kattsun
*    created: 24-04-2021 21:20:02
"""


def main():
    N = int(input())
    S = input().strip()
    Q = int(input())
    keys = list(range(1, N*2 + 1))
    D = dict(zip(keys, S))
    for i in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            a, b = D[A], D[B]
            D[A], D[B] = b, a
        else:
            S = ''.join(D.values())
            S = S[N:] + S[:N]
            D = dict(zip(keys, S))
    print(''.join(D.values()))


if __name__ == '__main__':
    main()
