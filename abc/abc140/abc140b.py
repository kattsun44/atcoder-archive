def main():
    n = int(input())
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    C = list(map(int, input().split(' ')))
    ans = 0

    for i in range(n):
        # A[i]番目の満足度を足す
        ans += B[A[i] - 1]
        # もし2皿目以降で食べた料理の番号が連番だったら
        if i >= 1 and A[i] - A[i - 1] == 1:
            # A[i] - 1 番目のボーナス満足度を足す
            ans += C[A[i] - 2]
    
    print(ans)

if __name__ == '__main__':
    main()  