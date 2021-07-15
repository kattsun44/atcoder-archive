"""
*    author:  kattsun
*    created: 16-07-2021 07:42:56
"""
from collections import deque
def main():
    N, Q = map(int, input().split())
    A = deque(map(int, input().split()))
    for i in range(Q):
        T, x, y = map(int, input().split())
        if T == 1:
            toY = A[y-1]
            toX = A[x-1]
            A[x-1] = toY
            A[y-1] = toX
        elif T == 2:
            A.rotate()
        else:
            print(A[x-1])


if __name__ == '__main__':
    main()