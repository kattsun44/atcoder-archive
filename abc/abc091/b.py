def main():
    n = int(input())
    dn = {}
    for i in range(n):
        w = input().strip()
        if w in dn:
            dn[w] += 1
        else:
            dn[w] = 1

    m = int(input())
    for i in range(m):
        w = input().strip()
        if w in dn:
            dn[w] -= 1
        else:
            dn[w] = -1
    
    print(max(max(dn.values()), 0))

if __name__ == '__main__':
    main()