import math
def main():
    a, b, t = list(map(int, input().split(' ')))
    
    print(math.floor(t / a) * b)

if __name__ == '__main__':
    main()