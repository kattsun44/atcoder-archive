def main():
    n = list(map(int, input().split(' ')))
    ans = 15 - sum(n)
    
    print(ans)

if __name__ == '__main__':
    main()