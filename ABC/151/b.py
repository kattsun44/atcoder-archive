def main():
    n, k, m = list(map(int, input().split(' ')))
    t = sum(list(map(int, input().split(' '))))
    ans = n * m - t if n * m - t >= 0 else 0
    ans = -1 if ans > k else ans
    
    print(ans)

if __name__ == '__main__':
    main()