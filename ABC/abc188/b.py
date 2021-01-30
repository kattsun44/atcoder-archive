def main():
    n = int(input())
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    total = 0

    for i in range(n):
        total += A[i] * B[i]
    
    ans = 'Yes' if total == 0 else 'No'

    print(ans)

if __name__ == '__main__':
    main()