def main():
    a, b = list(map(int, input().split(' ')))

    ans = a - 1 if a > b else a
    
    print(ans)

if __name__ == '__main__':
    main()