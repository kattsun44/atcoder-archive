import math
def main():
    A,B,X = list(map(int, input().split(' ')))
    ans = 0

    for i in range(1000000):

        # Nの桁数を仮決め
        dN = len(str(i))
        N = math.floor((X - B * dN) / A)
        N = min([N,1000000000]) #売られている最大値

        # 実際のNの価格
        priceN = A * N + B * len(str(N))

        # X以下で買え、かつ最大のN
        if priceN <= X and N > ans:
            ans = N
    
    print(ans)

if __name__ == '__main__':
    main()