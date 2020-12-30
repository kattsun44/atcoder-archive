def main():
    a, b, x = list(map(int, input().split(' ')))
    
    if a <= x and a + b >= x:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()