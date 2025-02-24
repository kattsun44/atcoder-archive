"""
*    author:  kattsun
*    created: 06-06-2021 10:09:01
"""
from itertools import combinations


def main():
    N = int(input())
    A = []
    for i in range(N):
        x, y = map(int, input().split())
        A.append((x, y))
    # x座標, y座標それぞれの昇順にソート
    X = sorted(A, key=lambda x: x[0])
    Y = sorted(A, key=lambda x: x[1])
    if N > 4:
        X = X[:2] + X[-2:]
        Y = Y[:2] + Y[-2:]
    # Xからはx座標、Yからはy座標のみ抽出し、組み合わせリストを作成
    comb_X = list(combinations([x[0] for x in X], 2))
    comb_Y = list(combinations([y[1] for y in Y], 2))
    B = []
    for i in range(len(comb_X)):
        B.append(abs(comb_X[i][0] - comb_X[i][1]))
        B.append(abs(comb_Y[i][0] - comb_Y[i][1]))
    B.sort(reverse=True)
    print(B[1])


if __name__ == '__main__':
    main()
