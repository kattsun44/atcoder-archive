def main():
    X, N = list(map(int, input().split()))
    if N != 0:
        P = list(map(int, input().split()))
    else:
        print(X)
        return

    # 増加分と減少分のリストを作成
    X = [X, X]
    
    for i in range(N + 1):
        # XがPに含まれていなければ出力
        if X[0] not in P:
            print(X[0])
            return
        elif X[1] not in P:
            print(X[1])
            return
        # XがPに含まれていればインクリメント&デクリメント
        else:
            X[0] -= 1
            X[1] += 1

if __name__ == '__main__':
    main()