"""
*    author:  kattsun
*    created: 09-02-2021 17:09:37
"""
from math import gcd
def lcm(x,y): return x*y/gcd(x,y)

def main():
    a = int(input())
    b = int(input())
    n = int(input())
    ans = lcm(a,b) * (n+lcm(a,b)+1)/lcm(a,b)
    print(ans)

if __name__ == '__main__':
    main()