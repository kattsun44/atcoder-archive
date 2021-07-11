"""
*    author:  kattsun
*    created: 10-07-2021 21:20:46
"""
import sys
sys.setrecursionlimit(10**8)

dep = dict()

def dfs(G, s, _dep=0, p=-1):
    dep[s] = _dep
    for u in G[s]:
        # print(u, p,_dep)
        if u == p: continue
        dfs(G, u, _dep+1, s)

def main():
    N, Q = map(int, input().split())
    G = [set() for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].add(b-1)
        G[b-1].add(a-1)
    dfs(G, 0)
    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if (dep[c] + dep[d]) % 2 == 1:
            print('Road')
        else:
            print('Town')

if __name__ == '__main__':
    main()