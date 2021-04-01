def main():
    n, T = list(map(int, input().split(' ')))
    d = dict()

    for i in range(n):
        c, t = list(map(int, input().split(' ')))
        if t <= T:
            d[c] = t
    
    if len(d) == 0:
        print('TLE')
    else:
        print(min(d.keys()))

if __name__ == '__main__':
    main()