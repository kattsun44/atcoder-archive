def main():
    n = int(input())
    k = int(input())
    X = list(map(int, input().split(' ')))
    total = 0

    for i in range(n):
        total += min([(abs(0-X[i]) * 2), (abs(k-X[i]) * 2)])
    
    print(total)

if __name__ == '__main__':
    main()