"""
*    author:  kattsun
*    created: 12-03-2021 20:07:31
"""
import math
def main():
    a,b,c,d = map(int, input().split())
    e = c*d // math.gcd(c,d)
    a -= 1

    aa = a - (a//c + a//d - a//e)
    bb = b - (b//c + b//d - b//e)

    print(bb-aa)

if __name__ == '__main__':
    main()