def main():
    n = input().strip()
    N = n.upper()
    uc = 0
    cc = 0

    if n[0] != 'A':
        print('WA')
        return

    for i in range(len(n)):
        if n[i] == N[i]:
            uc += 1
        if 2 <= i <= len(n) - 2:
            if n[i] == 'C':
                cc += 1
    
    if uc == 2 and cc == 1:
        print('AC')
    else:
        print('WA')
    

if __name__ == '__main__':
    main()