"""
*    author:  kattsun
*    created: 31-01-2021 19:05:19
"""
import math
import itertools
def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for i in range(n)]
    total_l = 0
    cnt = 0

    for order in itertools.permutations(points, n):
        l = 0
        for i in range(n-1):
            l += math.sqrt((order[i][0] - order[i+1][0])**2 + (order[i][1] - order[i+1][1])**2)
        total_l += l
        cnt += 1
    print(total_l/cnt)


if __name__ == '__main__':
    main()