"""
*    author:  kattsun
*    created: 04-07-2021 21:41:12
"""
from pprint import pprint
def main():
    N, M = map(int, input().split())
    G = dict()
    for i in range(N):
        G[i] = dict()
    for i in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        G[A][B] = C
    pprint(G)

if __name__ == '__main__':
    main()