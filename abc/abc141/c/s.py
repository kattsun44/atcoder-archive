"""
*    author:  kattsun
*    created: 16-05-2021 09:59:16
"""


def main():
    N, K, Q = map(int, input().split())
    point = [0] * N
    for i in range(Q):
        A = int(input())
        point[A - 1] += 1
    for i in range(N):
        if point[i] + K - Q > 0:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
