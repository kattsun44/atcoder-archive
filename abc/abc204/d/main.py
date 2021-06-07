"""
*    author:  kattsun
*    created: 06-06-2021 22:17:08
"""
from collections import defaultdict, deque


def main():
    N = int(input())
    A = list(map(int, input().split()))
    DA = deque(sorted(A, reverse=True))
    B = DA[0]
    DA.popleft()
    C = 0
    # for i in range(N):
    #     if B <= sum(DA):
    #         C += DA[0]
    #     else:
    #         if DA


if __name__ == '__main__':
    main()
