def main():
    x, a = list(map(int, input().split(' ')))
    ans = 0 if x < a else 10
    print(ans)

if __name__ == '__main__':
    main()