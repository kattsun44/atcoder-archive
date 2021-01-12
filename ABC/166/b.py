def main():
    n, k = list(map(int, input().split(' ')))
    candy = []
    owners = []
    cnt = 0
    
    for i in range(k * 2):
        if i % 2 == 1:
            candy.append(input())
            owners.append(list(map(int, input().split(' '))))
    owners = sum(owners, [])

    for i in range(n):
        if i + 1 not in owners:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()