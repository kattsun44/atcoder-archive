def main():
    n = int(input())
    ds = list(map(int, input().split(' ')))
    t = 0
    
    for i in range(n):
        for j in range(n - i - 1):
            t += ds[i] * ds[j + i + 1]
    print(t)

if __name__ == '__main__':
    main()