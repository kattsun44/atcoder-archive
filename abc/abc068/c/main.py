"""
*    author:  kattsun
*    created: 29-05-2021 15:39:22
"""


def main():
    N, M = map(int, input().split())
    P = set()
    Q = set()
    for i in range(M):
        a, b = map(int, input().split())
        if a == 1:
            P.add(b)
        if b == N:
            Q.add(a)
    if len(P & Q) >= 1:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')


if __name__ == '__main__':
    main()
