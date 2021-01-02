def main():
    n, m = list(map(int, input().split(' ')))
    s = set(list(range(1, n + 1)))

    for i in range(m):
        l, r = list(map(int, input().split(' ')))
        s2 = set(list(range(l, r + 1)))
        s = s & s2
    
    print(len(s))

if __name__ == '__main__':
    main()