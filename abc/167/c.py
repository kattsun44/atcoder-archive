"""
*    author:  kattsun
*    created: 16-01-2021 12:50:44
"""
import itertools
def main():
    n,m,x = map(int,input().split(' '))
    books = [list(map(int, input().split(' '))) for i in range(n)]
    ans = 1200001

    # 本の組み合わせを全探索
    for i in range(1, n+1):
        for j in itertools.combinations(books,i):
            L = list(j)

            # 各項目合算用リスト
            total = []
            [total.append(0) for i in range(m+1)]

            # 各項目を足していく
            for k in range(len(L)):
                for l in range(m+1):
                    total[l] += L[k][l]

            # 理解度が最低ラインxを超えている かつ 合計金額が安い場合のみans更新
            if min(total[1:]) >= x and total[0] < ans:
                ans = total[0]
    
    if ans != 1200001:
        print(ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()