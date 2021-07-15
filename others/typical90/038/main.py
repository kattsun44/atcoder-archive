"""
*    author:  kattsun
*    created: 16-07-2021 07:12:04
"""
import math
def lcm(x,y):
    return (x * y) // math.gcd(x, y)
def main():
    A, B = map(int, input().split())
    num = lcm(A, B)
    if num <= 1000000000000000000:
        print(num)
    else:
        print('Large')

if __name__ == '__main__':
    main()