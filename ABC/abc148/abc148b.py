def main():
    n = int(input())
    s, t = list(map(str.strip, input().split(' ')))
    ans = ''

    for i in range(n):
        ans = ans + s[i] + t[i]
    
    print(ans)

if __name__ == '__main__':
    main()