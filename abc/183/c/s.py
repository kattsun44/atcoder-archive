"""
*    author:  kattsun
*    created: 14-05-2021 08:04:55
"""
from itertools import permutations as pt
def main():
    N, K = map(int, input().split())
    T = []
    for i in range(N):
        T.append(list(map(int, input().split())))
    ans = 0

    # 途中地点のリスト
    point = [i for i in range(1, N)]
    # 通り方の数
    directions = pt(point)

    for d in directions:
        ttl = 0
        # スタート地点
        start = 0
        for j in range(len(d)):
            goal = d[j]
            ttl +=  T[start][goal]
            start = goal
        ttl += T[start][0]
        if ttl == K:
          ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()