def main():
    n = int(input())
    A = list(map(int, input().split(' ')))
    l = 0
    ans = 0

    for i in A:
        if i < l:
            ans += l - i
        if i > l:
            l = i            
    
    print(ans)

if __name__ == '__main__':
    main()