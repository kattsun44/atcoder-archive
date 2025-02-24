"""
*    author:  kattsun
*    created: 08-06-2021 07:31:44
"""
import sys
sys.setrecursionlimit(10000)

def iter_dfs(G, s):
    S, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        Q.extend(G[u])
        yield u

def main():
    N, M = map(int, input().split())
    G = [[] for i in range(N)]
    ans = 0
    for i in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
    for i in range(N):
        temp = [False] * N
        ans += len(list(iter_dfs(G, i)))
    print(ans)


if __name__ == '__main__':
    main()