def main():
    S, P = map(int, input().split())
    res = []
    for i in range(1, int(P ** 0.5) + 1):
        if P % i == 0:
            res.append(i)
            res.append(P // i)

    for x in res:
        if x + P // x == S:
            print('Yes')
            return
    print('No')
    return


if __name__ == '__main__':
    main()
