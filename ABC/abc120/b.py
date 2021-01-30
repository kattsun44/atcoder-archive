def main():
    a, b, k = list(map(int, input().split(' ')))
    L = []
    
    for i in range(b):
        if a % (i + 1) == 0 and b % (i + 1) == 0:
            L.append(i + 1)
    
    print(L[-k])

if __name__ == '__main__':
    main()