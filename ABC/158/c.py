import math
def main():
    A, B = map(int, input().split(' '))
    
    # A(B)とA+1(B+1)それぞれを税率の逆数で掛けた数を両端とする区間を作る
    sa = set(list(range(math.ceil(100 / 8 * A), 
                        math.floor(100 / 8 * (A + 1)))))
    sb = set(list(range(10 * B, 
                        10 * (B + 1))))

    # 区間にある最小かつ共通の整数が答え
    # もし共通する整数がなければ、-1を返す
    ans = min(sa & sb) if len(sa & sb) >= 1 else -1

    print(ans)

if __name__ == '__main__':
    main()