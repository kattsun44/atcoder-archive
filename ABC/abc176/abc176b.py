def main():
    n = list(map(int, list(input())))
    t = sum(n)
    print('Yes' if t % 9 == 0 else 'No')

if __name__ == '__main__':
    main()