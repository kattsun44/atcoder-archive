def main():
    n = int(input())
    D = []
    cnt = 0

    for i in range(n):
        x, y = list(map(int, input().split(' ')))
        D.append([x, y])
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            x0 = D[i][0]
            y0 = D[i][1]
            x1 = D[j][0]
            y1 = D[j][1]
            s = (y1 - y0) / (x1 - x0)
            if abs(s) <= 1:
                cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()