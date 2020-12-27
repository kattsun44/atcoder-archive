def main():
    a, b, c = list(map(int, input().split(' ')))
    ans = c - (a - b)
    ans = 0 if ans < 0 else ans
    
    print(ans)

if __name__ == '__main__':
    main()