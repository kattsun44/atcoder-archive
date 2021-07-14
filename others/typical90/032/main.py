"""
*    author:  kattsun
*    created: 15-07-2021 07:50:02
"""
from itertools import permutations
def main():
    N = int(input())
    runnner = []
    for _ in range(N):
        runnner.append(list(map(int, input().split())))
    M = int(input())
    G = [[] for _ in range(N)]
    for _ in range(M):
        X, Y = map(int, input().split())
        G[X-1].append(Y-1)
        G[Y-1].append(X-1)
    
    # 走順のパターン
    patterns = list(permutations([i for i in range(N)]))
    # いい走順を判定していく
    good_patterns = []
    for p in patterns:
        is_good_p = True

        # 隣同士の選手を調べる
        for i in range(len(p)-1):
            pair = (p[i], p[i+1])
            if pair[1] in G[pair[0]]: # もし嫌いな選手同士なら
                is_good_p = False
                continue
        if is_good_p:
            good_patterns.append(p)

    # いい走順がない場合、-1を出力
    if good_patterns == []:
        print(-1)
        return

    answers = []
    for gp in good_patterns:
        time = 0
        for i in range(len(gp)):
            time += runnner[gp[i]][i]
        answers.append(time)
    print(min(answers))


if __name__ == '__main__':
    main()