def main():
    n = int(input())
    L = list(map(int, input().split(' ')))
    l = max(L)
    L.remove(l)
    ans = 'Yes' if l < sum(L) else 'No'

    print(ans)

if __name__ == '__main__':
    main()