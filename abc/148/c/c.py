from math import gcd
def main():
    a, b = list(map(int, input().split(' ')))
    GCD = gcd(a, b)
    print(int(a * b / GCD))

if __name__ == '__main__':
    main()