def main():
    L = list(map(int, input().split(' ')))
    k = int(input())
    d = max(L)
    
    for i in range(k):
        d = d * 2

    print(sum(L) + d - max(L))

if __name__ == '__main__':
    main()