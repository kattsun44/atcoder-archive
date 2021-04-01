def main():
    n = int(input())
    V = list(map(int, input().split(' ')))
    C = list(map(int, input().split(' ')))
    total = 0
    
    for i in range(n):
        d = V[i] - C[i]
        total += d if d > 0 else 0
    print(total)

if __name__ == '__main__':
    main()