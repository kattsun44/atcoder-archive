def main():
    n = int(input())
    A = list(map(int, input().split(' ')))
    A.sort(reverse=True)

    p1 = []
    p2 = []
    
    for i in range(n):
        if i % 2 == 0:
            p1.append(A[i])
        else:
            p2.append(A[i])

    print(sum(p1)- sum(p2))

if __name__ == '__main__':
    main()