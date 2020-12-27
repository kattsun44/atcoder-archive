def main():
    n, k = list(map(int, input().split(' ')))
    s = input().strip()
    ans =''

    for i in range(n):
        ans += s[i].lower() if i + 1 == k else s[i]
    
    print(ans)

if __name__ == '__main__':
    main()