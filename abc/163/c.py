def main():
    n = int(input())
    A = list(map(int, input().split(' ')))
    cnts = dict(zip(range(1, n + 1), [0] * n))

    for i in range(n-1):
        cnts[A[i]] += 1

    for cnt in cnts.values():
        print(cnt)

if __name__ == '__main__':
    main()