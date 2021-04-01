def main():
    a, b, k = list(map(int, input().split(' ')))

    L = []
    
    for i in range(min(b, k)):
        if a + i not in L and a <= a + i <= b:
            L.append(a + i)
        if b - i not in L and a <= b - i <= b:
            L.append(b - i)
    
    L.sort()
    for i in L:
        print(i)
    

if __name__ == '__main__':
    main()