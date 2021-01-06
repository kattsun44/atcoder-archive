def main():
    s = input().strip()
    t = input().strip()
    
    for i in s:
        for j in t:
            if i < j:
                print('Yes')
                return

    if len(set(list(s+t))) == 1 and len(s) < len(t):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()