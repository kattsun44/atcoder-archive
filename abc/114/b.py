def main():
    n = input().strip()
    L = []

    for i in range(len(n) - 2):
        a = int(n[i:i + 3])
        L.append(abs(a - 753))

    print(min(L))
    

if __name__ == '__main__':
    main()