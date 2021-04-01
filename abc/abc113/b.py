def main():
    n = int(input())
    t, a = list(map(int, input().split(' ')))
    H = list(map(int, input().split(' ')))
    L = []

    for i in range(n):
        L.append(abs((t - H[i] * 0.006) - a))
    
    print(L.index(min(L)) + 1)

if __name__ == '__main__':
    main()