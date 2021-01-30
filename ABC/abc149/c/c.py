def main():
    X = int(input())

    if X == 2:
        print(2)
        return

    while True:
        for i in range(2, int(X/2)):
            if X % i == 0 or X % (int(X/2) - i + 2) == 0:
                break
            if i + 1 == int(X/2):
                print(X)
                return
        X += 1
    print(n)

if __name__ == '__main__':
    main()