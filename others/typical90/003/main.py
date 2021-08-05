"""
*    author:  kattsun
*    created: 05-08-2021 08:10:23
"""


from collections import deque


def main():
    N = int(input())
    G = [[] for i in range(N)]
    for _ in range(N-1):
        A, B = map(int, input().split())
        G[A-1].append(B-1)
        G[B-1].append(A-1)

    def bfs(s):
        inf = float('inf')
        dist = [inf] * N  # dist: 頂点sからの距離の記録
        dist[s] = 0       # 頂点s自身の距離は0
        q = deque([s])
        while q:
            # u: 今調べている頂点, v: 頂点uに隣接している頂点
            u = q.popleft()
            for v in G[u]:
                """
                頂点vは頂点uと隣接しているため、dist[v] > dist[u]+1 であれば、
                頂点sからの距離 dist[v]は dist[u] + 1 になる (1だけ深くなる)

                dist[v] > dist[u]+1 になる場合
                1) 頂点vが未調査 (=inf) のとき
                2) 別の頂点から遠回りした結果が記録されているとき
                """
                if dist[v] > dist[u] + 1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist
    dist1 = bfs(0)
    max_d, s = 0, 0
    for i, d in enumerate(dist1):
        if max_d < d:
            max_d = d
            s = i
    dist2 = bfs(s)
    print(max(dist2)+1)


if __name__ == '__main__':
    main()
