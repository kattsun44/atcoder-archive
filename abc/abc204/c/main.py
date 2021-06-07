"""
*    author:  kattsun
*    created: 06-06-2021 21:03:53
"""
import networkx as nx


def main():
    N, M = map(int, input().split())
    ans = N
    DG = nx.DiGraph()
    DG.add_nodes_from(range(1, N + 1))
    for i in range(M):
        a, b = map(int, input().split())
        DG.add_edge(a, b)
    for i in range(M):
        for j in range(M):
            for path in nx.all_simple_paths(DG, source=i+1, target=j+1):
                if path:
                    ans += 1
    print(ans)


if __name__ == '__main__':
    main()
