"""
*    author:  kattsun
*    created: 10-07-2021 21:20:46
"""
import sys
sys.setrecursionlimit(10**8)


def depth_by_dfs(G, s, seen=None, _dep=0, dep=None):
    if dep == None: dep = dict()
    if seen == None: seen = set()
    seen.add(s)
    dep[s] = _dep
    for u in G[s]:
        if u in seen: continue
        depth_by_dfs(G, u, seen, _dep+1, dep)
    return dep

def main():
    N, Q = map(int, input().split())
    G = [set() for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].add(b-1)
        G[b-1].add(a-1)
    dep = depth_by_dfs(G, 0)
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