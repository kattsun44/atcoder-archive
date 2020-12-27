def main():
    n = int(input())
    d = {}
    L = []
    for i in range(n):
        L.append((input().sprit(' ')))

        # 値はリストで持ち、重複したキーが出てきたらリストに追加
        if s not in d:
            d[s] = [int(p.strip())]
        else:
            d[s].append(int(p.strip()))
    
    # 辞書順のタプルにする
    d = sorted(d.items())

    for i in range(len(d)):
        # 値降順でソート
        d[i][1].sort(reverse=True)
        # 当てはまるLのインデックスを出力
        for j in range(len(d[i][1])):
            print(L.index(d[i][0] + ' ' + str(d[i][1][j])) + 1)
    
if __name__ == '__main__':
    main()