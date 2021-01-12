def main():
    n, m = map(int, input().split(' '))
    idx = list(range(1, n + 1))
    H = dict(zip(idx, list(map(int, input().split(' ')))))
    cnts = dict(zip(idx, [0] * (n + 1)))
    
    for _ in range(m):
        a, b = map(int, input().split(' '))
        if H[a] > H[b]:
            cnts[b] += 1
        elif H[a] < H[b]:
            cnts[a] += 1
        else:
            cnts[a] += 1
            cnts[b] += 1

    print(list(cnts.values()).count(0))

if __name__ == '__main__':
    main()