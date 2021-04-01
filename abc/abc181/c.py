def main():
    n = int(input())
    X = []
    Y = []
    coordinates = []

    for i in range(n):
        x,y = map(int,input().split(' '))
        coordinates.append(tuple([x,y]))

        # 同じX(Y)座標が3つ以上あればYesを出力
        if X.count(x) == 2 or Y.count(y)==2:
            print('Yes')
            return
        X.append(x)
        Y.append(y)

    # 2直線の傾きを比較し、同じならYesを出力
    for i in range(n):
        x1,y1 = coordinates[i]
        for j in range(n-i-1):
            x2,y2 = coordinates[i+j+1]
            for k in range(n-i-j-2):
                x3,y3 = coordinates[i+j+k+2]

                # ゼロ除算にならない場合のみ計算
                if x1 != x2 and x1 != x3:
                    a12 = (y2-y1)/(x2-x1)
                    a13 = (y3-y1)/(x3-x1)
                    if a12 == a13:
                        print('Yes')
                        return
    
    print('No')

if __name__ == '__main__':
    main()