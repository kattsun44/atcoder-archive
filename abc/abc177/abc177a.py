def main():
    d, t, s = list(map(int, input().split(' '))) 
    if d / s <= t:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()