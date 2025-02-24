def main():
    k, n = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    a.append(k + a[0])
    
    # 2点間距離のリスト
    d = []

    for i in range(n):
        d.append(abs(a[i] - a[i+1]))
    d.remove(max(d))
    print(sum(d))

if __name__ == '__main__':
    main()