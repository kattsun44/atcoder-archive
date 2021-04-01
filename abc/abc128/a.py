import math
def main():
    a, p = list(map(int, input().split(' ')))
    
    print(math.floor((a * 3 + p) / 2))

if __name__ == '__main__':
    main()