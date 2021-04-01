def main():
    n = int(input())
    s = input().strip()
    ss = set(list(s))
    L = []
    
    for i in range(n - 1):
        x = s[i + 1:]
        y = s[:i + 1]
        p = len(set(list(x)) & set(list(y)))
        L.append(p)

    print(max(L))

if __name__ == '__main__':
    main()