"""
*    author:  kattsun
*    created: 19-06-2021 21:23:04
"""
from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())


def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 種類数が頂点の数
    uf = UnionFind(len(set(A)))
    # 頂点の数字と番号のペア
    d = {x: i for i, x in enumerate(set(A))}

    first = A[:N//2]
    last = A[-(-N//2):]
    last_reverse = list(reversed(last))

    for i in range(N//2):
        uf.union(d[first[i]], d[last_reverse[i]])

    print(len(set(A)) - uf.group_count())


if __name__ == '__main__':
    main()
