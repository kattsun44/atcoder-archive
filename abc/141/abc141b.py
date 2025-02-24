def main():
    s = input().strip()
    os = ['R', 'U', 'D']
    es = ['L', 'U', 'D']
    
    for i in range(len(s)):
        if (i + 1) % 2 == 1:
            if s[i] not in os:
                print('No')
                return
        else:
            if s[i] not in es:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()