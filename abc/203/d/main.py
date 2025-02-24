"""
*    author:  kattsun
*    created: 30-05-2021 22:01:03
"""
import numpy as np
from statistics import median
import itertools


def main():
    N, K = map(int, input().split())
    board = []
    ans = 10000000000
    for i in range(N):
        board.append(list(map(int, input().split())))
    array = np.array(board)
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            pond = array[i:i+K, j:j+K]
            pond_flatten = list(itertools.chain.from_iterable(pond.tolist()))
            l = len(pond_flatten)
            ans = min(ans, pond_flatten[l//2])
    print(ans)


if __name__ == '__main__':
    main()
