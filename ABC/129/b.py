def main():
    n = int(input())
    W = list(map(int, input().split(' ')))
    d = []

    for i in range(n - 1):
        s1 = sum(W[:i + 1])
        s2 = sum(W[i + 1:])
        d.append(abs(s1 - s2))

    print(min(d))

if __name__ == '__main__':
    main()