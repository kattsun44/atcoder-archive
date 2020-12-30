def main():
    d, n = list(map(int, input().split(' ')))

    a = 100 ** d
    
    print(a * n + int(n / 100) * a)

if __name__ == '__main__':
    main()