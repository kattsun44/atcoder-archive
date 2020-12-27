def main():
    n, l = list(map(int, input().split(' ')))
    L = []
    ans = 0

    for i in range(n):
        L.append(l + i)
    
    minDiff = abs(sum(L))

    for i in range(n):
        s = sum(L[:i] + L[i + 1:]) # i番目以外のりんごの美味しさの合計
        
        # sum(L) と s の差が小さい場合更新
        if abs(sum(L) - s) <= minDiff:
            minDiff = abs(sum(L) - s)
            ans = s

    print(ans)


if __name__ == '__main__':
    main()