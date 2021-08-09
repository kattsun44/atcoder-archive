"""
*    author:  kattsun
*    created: 09-08-2021 18:20:03
"""
from collections import deque


def bfs(G, s):
    inf = float('inf')
    dist = [inf] * 4  # dist: 頂点sからの距離の記録
    dist[s] = 0       # 頂点s自身の距離は0
    q = deque([s])
    while q:
        # u: 今調べている頂点, v: 頂点uに隣接している頂点
        u = q.popleft()
        for v in G[u]:
            if dist[v] > dist[u] + 1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def main():
    G = [[] for i in range(4)]
    for _ in range(3):
        A, B = map(int, input().split())
        G[A-1].append(B-1)
        G[B-1].append(A-1)
    dist = 0
    for i in range(4):
        dist = max(dist, max(bfs(G, i)))

    if dist == 3:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
