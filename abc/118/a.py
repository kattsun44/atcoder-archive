def main():
    a, b = list(map(int, input().split(' ')))
    ans = a + b if b % a == 0 else b - a
    print(ans)

if __name__ == '__main__':
    main()