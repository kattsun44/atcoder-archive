def main():
    N, C = list(map(int, input().split(' ')))
    As = []
    Bs = []
    Cs = []
    s = set() # 開始日と終了日のセット

    for i in range(N):
        a, b, c = list(map(int, input().split(' ')))
        As.append(a)
        Bs.append(b + 1)
        Cs.append(c)
        s.add(a)
        s.add(b + 1)
    
    ls = sorted(list(s))

    cost = [] # ls の区間ごとのコスト
    total = 0

    for i in range(len(ls) - 1):
        start = ls[i]
        end = ls[i + 1]
        # 開始するサービスの費用をcostにアペンド
        if start in As:
            cost.append(Cs[As.index(start)])
        # costのトータルよりすぬけプライムの方が安ければプライム費用を足す
        if sum(cost) > C:
            total += C * (end - start)
        else:
            total += sum(cost) * (end - start)
        # 終了するサービスの費用をcostから削除
        if end in Bs:
            cost.remove(Cs[Bs.index(end)])

    print(total)


if __name__ == '__main__':
    main()