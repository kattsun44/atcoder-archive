def main():
    n, m = list(map(int, input().split(' ')))
    A = []
    B = []
    cnt = 0

    for _ in range(n):
        A.append(input().strip())
    for _ in range(m):
        B.append(input().strip())

    # 画像Aの中で画像Bを縦横にn-m+1回動かして比較
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            if A[i][j] == B[0][0]:
                for k in range(m):
                    for l in range(m):
                        if A[i + k][j + l] ==B[k][l]:
                            cnt += 1
                    if cnt == m ** 2:
                        print('Yes')
                        return
                cnt = 0

    print('No')

if __name__ == '__main__':
    main()