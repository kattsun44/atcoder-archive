def main():
    a, b, c, d = list(map(int, input().split(' ')))

    if abs(c - a) <= d or abs(b - a) <= d and abs(c - b) <= d:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()