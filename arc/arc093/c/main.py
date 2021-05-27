"""
*    author:  kattsun
*    created: 27-05-2021 08:36:44
"""


def main():
    N = int(input()) + 2
    A = [0] + list(map(int, input().split()))
    A.append(0)
    ttl = 0
    a = 0
    for i in range(N):
        b = A[i]
        ttl += abs(a - b)
        a = b
    for i in range(1, N-1):
        print(ttl + abs(A[i-1]-A[i+1]) -
              abs(A[i] - A[i-1]) - abs(A[i] - A[i+1]))


if __name__ == '__main__':
    main()
