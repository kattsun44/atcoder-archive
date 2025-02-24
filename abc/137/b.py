def main():
    k, x = list(map(int, input().split(' ')))
    s = k * 2 -1
    ans = ''

    for i in range(s):
        ans += str(x - k + i + 1)
        ans += ' '

    print(ans)


if __name__ == '__main__':
    main()