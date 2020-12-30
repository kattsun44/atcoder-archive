def main():
    a, b = list(map(int, input().split(' ')))
    ans = [a + b, a - b, a * b]
    print(max(ans))

if __name__ == '__main__':
    main()