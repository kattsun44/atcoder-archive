def main():
    a, b = list(map(int, input().split(' ')))
    
    # 隣り合った塔の差の2乗が塔の高さの合計
    # 合計から aとbを引いた残りを2で割ったものが答え
    print(int(((b - a) ** 2 - (a + b)) / 2))

if __name__ == '__main__':
    main()