def main():
    # n番目のリュカ数を求める
    n = int(input())
    L0 = 2
    L1 = 1
    ans = L1

    for i in range(n - 1):
        ans = L0 + L1
        L0 = L1
        L1 = ans
    
    print(ans)

if __name__ == '__main__':
    main()