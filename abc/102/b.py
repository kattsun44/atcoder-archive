def main():
    n = input()
    L = list(map(int, input().split(' ')))
    
    print(max(L) - min(L))

if __name__ == '__main__':
    main()