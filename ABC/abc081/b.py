def main():
    n = int(input())
    A = list(map(int, input().split(' ')))
    cnt = 0
    
    while True:
        for i in range(n):
            if A[i] % 2 != 0:
                print(cnt)
                return
        cnt += 1
        A = list(map(lambda x: x/2, A))

    print(cnt)

if __name__ == '__main__':
    main()