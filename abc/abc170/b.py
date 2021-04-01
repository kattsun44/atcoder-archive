def main():
    x, y = list(map(int, input().split(' ')))
    
    for i in range(x + 1):
        foots = 2 * i + 4 * (x - i)
        if foots == y:
            print('Yes')
            break
        elif i == x:
            print('No')

if __name__ == '__main__':
    main()