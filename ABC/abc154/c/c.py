def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    sA = set(A)
    
    ans = "YES" if len(A) == len(sA) else "NO"
    print(ans)

if __name__ == '__main__':
    main()