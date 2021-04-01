def main():
    n, m, c = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    t = 0
    cnt = 0

    for i in range(n):
        A = list(map(int, input().split(' ')))
        for j in range(m):
            t += A[j] * B[j]
        if t + c > 0:
            cnt += 1
        t = 0
    
    print(cnt)

if __name__ == '__main__':
    main()