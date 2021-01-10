import math
def main():
    x, y, z = list(map(int, input().split(' ')))
    
    if x % (y+z) >= z:
        print(math.floor(x / (y+z)))
    else:
        print(math.floor(x / (y+z)) - 1)


if __name__ == '__main__':
    main()