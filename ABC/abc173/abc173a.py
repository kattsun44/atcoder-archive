import math
def main():
    n = int(input())
    
    print(1000 * math.ceil(n / 1000) - n)

if __name__ == '__main__':
    main()