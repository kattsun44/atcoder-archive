import math
def main():
    n, d = list(map(int, input().split(' ')))
    
    print(math.ceil(n / (d * 2 + 1)))

if __name__ == '__main__':
    main()