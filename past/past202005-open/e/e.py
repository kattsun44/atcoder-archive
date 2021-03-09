"""
*    author:  kattsun
*    created: 10-03-2021 08:08:11
"""

def main():
    n,m,q = map(int, input().split())

    # N x N の隣接行列をつくる
    g = []
    for i in range(n):
        # 長さNの1次元配列をつくる
        row = []
        for j in range(n):
            row.append(0)
    
        # 長さNの1次元配列をgに追加する
        g.append(row)

    # M本の辺を受け取る
    for i in range(m):
        u,v = map(int, input().split())
    
        # 頂点番号はすべて-1
        u -= 1
        v -= 1

        # uv間は辺があるためTrue=1にする
        g[u][v] = 1
        g[v][u] = 1

    # 頂点の色のリストを受け取る
    c = list(map(int, input().split()))

    # q個のクエリを受け取る
    for i in range(q):
        query = list(map(int, input().split()))

        # スプリンクラーを起動するクエリの場合
        if query[0] == 1:
            x = query[1]

            # 頂点番号はすべて-1
            x -= 1

            # 頂点xの色を出力
            print(c[x])

            # すべての頂点を順番に見る
            for j in range(n):

                # 頂点jが頂点xに隣接しているとき、すなわち頂点xと頂点jの間に辺があるとき
                if g[x][j]:

                    # 頂点jの色をc[x]に置き換える
                    c[j] = c[x]
        
        # スプリンクラーを起動しない場合
        if query[0] == 2:
            x = query[1]
            y = query[2]
            x -= 1

            # 頂点xの色を出力
            print(c[x])

            # 頂点xの色をyに置き換える
            c[x] = y


if __name__ == '__main__':
    main()