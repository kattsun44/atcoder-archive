def main():
    a, b = list(map(int, input().split(' ')))
    aaa = int(str(a) * b)
    bbb = int(str(b) * a)
    print(max([aaa, bbb]))

if __name__ == '__main__':
    main()