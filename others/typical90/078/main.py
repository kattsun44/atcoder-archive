"""
*    author:  kattsun
*    created: 08-07-2021 08:22:15
"""


def main():
    N, M = map(int, input().split())
    G = []

    # 隣接リスト作成
    for i in range(N):
        G.append([])
    for i in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        G[A].append(B)
        G[B].append(A)

    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(len(G[i])):
            # 隣接した頂点が頂点の数値未満か
            if i > G[i][j]:
                cnt += 1
        # 頂点以下の隣接頂点が一つだけなら答えとしてカウント
        if cnt == 1:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
