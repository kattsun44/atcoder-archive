def main():
    p, q, r = list(map(int, input().split(' ')))
    
    print(min([p+q, q+r, r+p]))

if __name__ == '__main__':
    main()