def main():
    s = input().strip()
    t = input().strip()
    
    for i in range(len(s)):
        if s == t:
            print('Yes')
            return
        s = s[-1:] + s[:-1]

    print('No')

if __name__ == '__main__':
    main()