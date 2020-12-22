import numpy as np
def main():
    n = input()
    a = list(map(int, input().split(' ')))
    prod = np.prod(a)
    mn = 1000000000000000000
    
    if min(a) == 0:
        print(0)
    elif prod > mn:
        print(-1)
    else:
        print(prod)

if __name__ == '__main__':
    main()