def main():
    n, m, x = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    toN = []
    to0 = []

    for i in A:
        if i > x:
            toN.append(i)
        else:
            to0.append(i)
    
    print(min(len(toN), len(to0)))

if __name__ == '__main__':
    main()