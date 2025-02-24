def main():
    n, m = list(map(int, input().split(' ')))
    l = []
    cnt = 0

    for _ in range(n):
        l.append(2)
    for _ in range(m):
        l.append(1)

    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if (l[i] + l[j + 1 + i]) % 2 == 0:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()