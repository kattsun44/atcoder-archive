def main():
    n = int(input())
    L = []

    for i in range(n):
        L.append(int(input()))
    
    L[L.index(max(L))] = int(max(L) / 2)
    
    print(sum(L))

if __name__ == '__main__':
    main()