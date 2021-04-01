def main():
    n = int(input())
    ans = set()
    
    for i in range(n):
        if (i + 1) ** 2 > n:
            break
        if n % (i + 1) == 0:
            ans.add(i + 1)
            ans.add(int(n/(i + 1)))
    ans = list(ans)
    ans.sort()

    for i in ans:
        print(i)

if __name__ == '__main__':
    main()