def main():
    n = int(input())
    s = input().strip()
    if n % 2 == 1:
        print('No')
        return
    
    fh = s[:int(n / 2)]
    lh = s[-int(n / 2):]

    if fh == lh:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()