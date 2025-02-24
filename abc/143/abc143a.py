def main():
    a, b = list(map(int, input().split(' ')))
    r = a - b * 2 if (a - b * 2) > 0 else 0
    print(r)

if __name__ == '__main__':
    main()