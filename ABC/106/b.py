def main():
    n = int(input())
    cnt = 0

    for i in range(n):
        div = 0 # 約数の数
        for j in range(i):
            s = (i + 1) / (j + 1)
            # sが割り切れていてかつ奇数のときのみ約数としてカウント
            if s.is_integer() and s % 2 == 1:
                div += 1
        if div == 7:
            cnt += 1
    
    print(cnt)


if __name__ == '__main__':
    main()