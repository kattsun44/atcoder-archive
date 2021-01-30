def main():
    n = int(input())
    A = list(map(int, input().split(' ')))
    rA = list(map(lambda x: 1/x, A))
    ans = 1 / sum(rA)
    
    print(ans)

if __name__ == '__main__':
    main()