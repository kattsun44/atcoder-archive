"""
*    author:  kattsun
*    created: 24-07-2021 10:16:32
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    target = sum(A) / 10
    A2 = A + A
    l = [0] * N * 2
    for i in range(N*2):
        ttl = 0
        for j in range(i, N*2):
            ttl += A2[j]
            if ttl == target:
                print('Yes')
                return
            elif ttl > target:
                break
    print('No')


if __name__ == '__main__':
    main()
