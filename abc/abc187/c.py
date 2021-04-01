def main():
    n = int(input())
    S1 = set()
    S2 = set()

    for i in range(n):
        w = input().strip()
        S1.add(w)
        if w[0] != '!':
            S2.add('!' + w)
        else:
            S2.add(w)

    if len(S1) == len(S2):
        print('satisfiable')
    else:
        S3 = S1 - S2
        for i in S3:
            if '!' + i in S1:
                print(i)
                return

if __name__ == '__main__':
    main()