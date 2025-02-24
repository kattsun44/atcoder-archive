def main():
    n = int(input())
    tA = 0
    tT = 0
    L = []
    cnt = 0
    
    if n == 1:
        print(1)
        return

    for i in range(n):
        a, b = list(map(int, input().split(' ')))
        tA += a
        L.append(a * 2 + b)

    L.sort(reverse=True)

    while tA >= tT:
        tT += L.pop(0)
        cnt += 1
    
    print(cnt)

if __name__ == '__main__':
    main()