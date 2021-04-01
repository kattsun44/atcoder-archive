def main():
    A, B, C, D = list(map(int, input().split(' ')))

    while (A > 0 or C > 0):
        C -= B
        if C <= 0:
            print('Yes')
            return
        A -= D
        if A <= 0:
            print('No')
            return
    

if __name__ == '__main__':
    main()