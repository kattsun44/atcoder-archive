import math
def main():
    n, k = list(map(int, input().split(' ')))
    
    print(math.ceil(n/k) - math.floor(n/k))

if __name__ == '__main__':
    main()