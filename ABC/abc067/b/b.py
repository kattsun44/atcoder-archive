def main():
    n,k = map(int, input().split(' '))
    L = list(map(int, input().split(' ')))
    L.sort(reverse=True)
    for i in range(n-k):
        L.pop()
    print(sum(L))

if __name__ == '__main__':
    main()