"""
*    author:  kattsun
*    created: 22-06-2021 07:39:46
"""

def main():
    N = int(input())
    c1 = [0] * N
    c2 = [0] * N
    ttl1 = 0
    ttl2 = 0
    for i in range(N):
        C, P = map(int, input().split())
        if C == 1:
            ttl1 += P
        else:
            ttl2 += P
        c1[i] = ttl1
        c2[i] = ttl2

    # index = 0 の場合を付与
    c1 = [0] + c1
    c2 = [0] + c2

    Q = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        print(c1[R]-c1[L-1], c2[R]-c2[L-1])


if __name__ == '__main__':
    main()