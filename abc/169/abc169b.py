def main():
    n = input()
    A = list(map(int, input().split(' ')))
    mn = 1000000000000000000
    
    if 0 in A:
        print(0)
        return
    
    prod = 1
    for a in A:
        prod *= a
        if prod > mn:
            print(-1)
            return

    print(prod)

if __name__ == '__main__':
    main()