def main():
    ks = list(map(str.strip, input().split(' ')))
    vs = list(map(int, input().split(' ')))
    d = dict(zip(ks, vs))
    w = input().strip()
    d[w] -= 1
    print(d.get(ks[0]), d.get(ks[1]))

if __name__ == '__main__':
    main()