def main():
    n = int(input())
    P = list(map(int, input().split(' ')))
    cnt = 0
    
    for i in range(n - 2):
        l = [P[i], P[i + 1], P[i + 2]]
        l.sort()
        if l[1] == P[i + 1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()