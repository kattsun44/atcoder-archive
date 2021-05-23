"""
*    author:  kattsun
*    created: 23-05-2021 09:09:09
"""
import decimal
from math import factorial
from decimal import Decimal


def main():
    a, b, k = map(int, input().split())
    ans = ''
    while a+b > 0:
        n = a + b - 1
        r = a - 1
        if a >= 1:
            x = (factorial(n) //
                 (factorial(r) * factorial(n - r)))
        if k <= x and a >= 1:
            ans += 'a'
            a -= 1
        else:
            ans += 'b'
            k -= x
            b -= 1
        # print(ans, x, k, a, b)
    print(ans)


if __name__ == '__main__':
    main()
