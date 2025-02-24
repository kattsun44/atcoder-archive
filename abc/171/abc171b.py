def main():
    n, k = list(map(int, input().split(' ')))
    pl = list(map(int, input().split(' ')))
    pl.sort()
    ans = sum(pl[:k])
    print(ans)

if __name__ == '__main__':
    main()