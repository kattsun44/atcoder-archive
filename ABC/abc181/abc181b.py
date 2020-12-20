def main():
    n = int(input())
    total = 0
    for i in range(n):
        a, b  = list(map(int, input().split(' ')))
        for j in range(b - a + 1):
            total += a + j
    print(total)

if __name__ == '__main__':
    main()