def main():
    L = list(map(int, input().split(' ')))
    
    print(max(L) * 9 + sum(L))

if __name__ == '__main__':
    main()