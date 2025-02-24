"""
*    author:  kattsun
*    created: 06-05-2021 07:01:04
"""
from collections import deque


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = deque()
    if N % 2 == 0:
        for i in range(N):
            if i % 2 == 0:
                B.append(A[i])
            else:
                B.appendleft(A[i])
    else:
        for i in range(N):
            if i % 2 != 0:
                B.append(A[i])
            else:
                B.appendleft(A[i])

    print(" ".join(map(str, list(B))))


if __name__ == '__main__':
    main()
