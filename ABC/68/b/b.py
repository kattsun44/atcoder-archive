def main():
    n = int(input())
    ans = 0
    max_cnt = 0
    
    for i in range(1, n+1):
        a = i
        cnt = 0
        while a >= 1:
            if a % 2 == 0:
                a /= 2
                cnt += 1
            else:
                break
        if cnt >= max_cnt:
            ans = i
            max_cnt = cnt

    print(ans)

if __name__ == '__main__':
    main()