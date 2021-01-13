def main():
    A, B = list(map(int, input().split(' ')))
    S = input().strip()

    if S[A] == '-': # A+1 文字目がハイフンかどうか
        DS = S.split('-')
        for i in DS:
            # ハイフンで分けた要素が数字かどうか判定
            if i.isnumeric() == False:
                print('No')
                return
        print('Yes')
    else:
        print('No')    

if __name__ == '__main__':
    main()