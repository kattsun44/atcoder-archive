import math
def main():
    a, b = list(map(str.strip, input().split(' ')))
    n = int(a + b)
    
    if math.sqrt(n).is_integer():
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()