def main():
    n, r = list(map(int, input().split(' ')))
    r = r if n >= 10 else r + 100 * (10 - n)
    print(r)

if __name__ == '__main__':
    main()