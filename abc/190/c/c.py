"""
*    author:  kattsun
*    created: 30-01-2021 21:08:23
"""

def main():
    n,m = list(map(int, input().split(' ')))
    ans = 0

    # 条件をタプルのリストで持つ
    cnds = []
    for i in range(m):
        cnds.append(tuple(map(int, input().split(' '))))

    # ボールを入れる選択肢をタプルのリストで持つ
    bowls = []
    k = int(input())
    for i in range(k):
        bowls.append(tuple(map(int, input().split(' '))))

    # ビットでボールの置き方の組合せを全探索
    for i in range(2**k):
        # ビット配列の作成
        bi = format(i,'b')
        bi = bi.zfill(k)
        bi = list(map(int,list(bi)))

        # 置いてある皿の番号のセット
        s = set()
        for j in range(k):
            s.add(bowls[j][bi[j]])

        # 条件が揃っていればインクリメント
        cnt = 0
        for j in range(m):
            if cnds[j][0] in s and cnds[j][1] in s:
                cnt += 1

        if ans < cnt:
            ans = cnt

    print(ans)

if __name__ == '__main__':
    main()