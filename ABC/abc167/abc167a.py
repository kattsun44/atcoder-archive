def main():
    s = input().strip()
    t = input().strip()
    
    if s == t[:-1]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()