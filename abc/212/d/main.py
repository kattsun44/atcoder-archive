"""
*    author:  kattsun
*    created: 31-07-2021 21:54:47
"""
import heapq


def main():
    Q = int(input())
    bag = []
    cnt = 0
    for _ in range(Q):
        S = input().strip()
        n = int(S[0])
        if len(S) != 1:
            x = int(S.split(' ')[-1])
        if n == 1:
            x -= cnt
            heapq.heappush(bag, x)
        elif n == 2 and len(bag):
            cnt += x
        elif n == 3 and len(bag):
            print(heapq.heappop(bag) + cnt)


if __name__ == '__main__':
    main()
