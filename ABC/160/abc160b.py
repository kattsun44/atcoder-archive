import math
def main():
    n = int(input())
    n500 = math.floor(n / 500)
    n5 = math.floor((n % 500) / 5)
    
    print(n500 * 1000 + n5  * 5)

if __name__ == '__main__':
    main()