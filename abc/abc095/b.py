import math
def main():
    n, x = list(map(int, input().split(' ')))
    L = []

    for i in range(n):
        L.append(int(input()))
    
    print(n + math.floor(((x - sum(L)) / min(L))))

if __name__ == '__main__':
    main()