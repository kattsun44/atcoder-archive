import itertools

def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m%n)

def main():
    k = int(input())
    total = 0

    for a in range(1, k+1):
        for b in range(1, k+1):
            for c in range(1, k+1):
                total += gcd(gcd(a, b), c)
    
    print(total)

if __name__ == '__main__':
    main()