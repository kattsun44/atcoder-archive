def main():
    n = int(input())
    d, x = list(map(int, input().split(' ')))
    cnt = 0

    for i in range(n):
        a = int(input())
        d_a = 1
        while d_a <= d:
            cnt += 1
            d_a += a
            pass
    
    print(cnt + x)

if __name__ == '__main__':
    main()