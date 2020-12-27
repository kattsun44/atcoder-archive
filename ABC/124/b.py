def main():
    n = int(input())
    H = list(map(int, input().split(' ')))
    cnt = 0
    pre = H[0]
    
    for i in range(n):
        if H[i] >= pre:
            cnt += 1
            pre = H[i]
    print(cnt)

if __name__ == '__main__':
    main()