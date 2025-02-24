def main():
    n = int(input())
    L = []

    for i in range(n):
        w = input().strip()
        if i != 0:
            if w in L or w[0] != s:
                print('No')
                return
            else:
                L.append(w)
        else:
            L.append(w)
        s = w[-1]
    print('Yes')
    

if __name__ == '__main__':
    main()