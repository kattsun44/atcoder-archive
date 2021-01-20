import itertools

def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m%n)

def main():
    k = int(input())
    L = list(range(1, k+1))

    for j in itertools.combinations(L, 3):
        print(list(j))

    
    print(L)

if __name__ == '__main__':
    main()