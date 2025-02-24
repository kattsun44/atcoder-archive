def main():
    n, k = list(map(int, input().split(' ')))
    cnt = 1

    while (n >   1):
        n = n / k
        if n >= 1:
            cnt += 1
        pass
    
    print(cnt)

if __name__ == '__main__':
    main()