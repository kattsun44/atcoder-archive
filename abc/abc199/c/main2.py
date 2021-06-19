"""
*    author:  kattsun
*    created: 19-06-2021 08:10:24
"""


def main():
    N = int(input())
    S = input().strip()
    Q = int(input())
    is_shifted = 0
    for i in range(Q):
        T, A, B = map(int, input().split())
        A -= 1
        B -= 1
        if T == 2:
            is_shifted += 1
            continue
        if is_shifted % 2 == 1:
            if A > N:
                A -= N
            else:
                A += N
            if B > N:
                B -= N
            else:
                B += N
        S = list(S)
        S[A], S[B] = S[B], S[A]
        S = ''.join(S)
    if is_shifted % 2 == 1:
        S = S[N:] + S[:N]
    print(S)


if __name__ == '__main__':
    main()
