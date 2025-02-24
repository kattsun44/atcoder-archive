def main():
    n, m = list(map(int, input().split(' ')))
    ans = 0
    cond = {}

    for i in range(m):
        s, c = map(int, input().split(' '))

        # 先頭に0をつけた表記は認めない
        if s == 1 and c == 0:
            # n = 1 以外の場合は
            if n != 1:
                print(-1)
                return

        # 同じ桁に違う数字を指定したらNG
        if s in cond and cond[s] != c:
            print(-1)
            return
        elif s not in cond:
            ans += 10 ** (n - s) * c

        cond[s] = c
    
    if ans < 10 ** (n - 1) and n != 1:
        print(ans + 10 ** (n - 1))
    else:
        print(ans)
    

if __name__ == '__main__':
    main()