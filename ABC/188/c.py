def main():
    n = int(input())
    l = 2 ** n
    A = list(map(int, input().split(' ')))

    A1 = set(A[0: int(l/2)])
    A2 = set(A[int(l/2):])
    
    print(A.index(min([max(A1), max(A2)])) + 1)

if __name__ == '__main__':
    main()