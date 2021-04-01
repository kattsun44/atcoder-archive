def main():
    a, b = list(map(int, input().split(' ')))
    cnt = 0
    for i in range(b - a + 1):
        s = str(a + i)
        if s[0] == s[-1] and s[1] == s[-2]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()