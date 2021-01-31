def main():
    s = input().strip()
    ss = set(s)
    
    if len(s) == len(ss):
        print('yes')
    else:
        print('no')

if __name__ == '__main__':
    main()