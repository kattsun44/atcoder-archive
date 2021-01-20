def main():
    n, m = list(map(int, input().split(' ')))
    v = list(map(int, input().split(' ')))
    vt = sum(v)

    for i in range(m):
        if max(v) / vt < 1 / (4 * m):
            print('No')
            return
        v.remove(max(v))

    print('Yes')

if __name__ == '__main__':
    main()