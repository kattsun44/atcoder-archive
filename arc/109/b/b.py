"""
*    author:  kattsun
*    created: 08-03-2021 21:18:57
"""
from decimal import Decimal
def quad_max(a,b,c):
    D=Decimal(b**2 - 4*a*c)**Decimal(1/2)
    return (-b+D)/(2*a)

def main():
    n = int(input())
    # 短い方から買わなくていい丸太の本数を求める
    a = quad_max(1,1,-n*2)
    print(n+1 - round(a))

if __name__ == '__main__':
    main()

