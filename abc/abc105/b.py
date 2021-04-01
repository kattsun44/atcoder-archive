def main():
    n = int(input())
    p = 3
    i = 0

    for i in range(n):
        for j in range(n):
            t = i * 4 + j * 7
            if t == n:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()