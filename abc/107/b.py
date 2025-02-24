def main():
    h, w = list(map(int, input().split(' ')))
    B = []
    hc = {} # 行方向のカウンタ
    wc = {} # 列方向のカウンタ

    for i in range(h):
        hc[i] = 0
    for i in range(w):
        wc[i] = 0
    
    for i in range(h):
        r = input().strip()
        B.append(r)

        # 白「.」マスをカウント
        for j in range(w):
            if r[j] == '.':
                hc[i] += 1
                wc[j] += 1

    for i in range(h):
        # 白マスの数が列数以下の行のみ
        if hc[i] != w:
            output = ''
            for j in range(w):
                # 白マスの数が行数以下の列をアウトプットに代入する
                if wc[j] != h:
                    output += B[i][j]
            print(output)

if __name__ == '__main__':
    main()