"""
*    author:  kattsun
*    created: 08-06-2021 07:31:44
"""
import sys
sys.setrecursionlimit(10000)

a,b,c,d,e,f,g,h = range(8)
G = [
    {b,c,d,e,f},  # a
    {c,e},        # b
    {d},          # c
    {e},          # d
    {f},          # e
    {c,g,h},      # f
    {f,h},        # g
    {f,g}         # h
]

def rec_dfs(G, s, S=None):
    if S is None: S = set()
    S.add(s)
    for u in G[s]:
        if u in S: continue
        rec_dfs(G, u, S)
    return S

def main():
    ans = 0
    for i in range(8):
        temp = [False] * 8
        print(list(rec_dfs(G, i)))


if __name__ == '__main__':
    main()