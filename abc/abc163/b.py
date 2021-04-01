def main():
    n = list(map(int, input().split(' ')))[0]
    d = list(map(int, input().split(' ')))
    s = sum(d)
    
    print(n - s) if n - s >= -1 else print(-1)

if __name__ == '__main__':
    main()