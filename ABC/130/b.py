def main():
    n, x = list(map(int, input().split(' ')))
    L = list(map(int, input().split(' ')))
    t = 0
    cnt = 1
    
    for i in range(n):
        t += L[i]
        if t > x:
            print(cnt)
            return
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()