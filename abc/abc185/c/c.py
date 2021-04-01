"""
*    author:  kattsun
*    created: 17-01-2021 09:14:48
"""
from math import comb
def main():
    L = int(input())
    ans = comb(L-1, 11)
    print(ans)

if __name__ == '__main__':
    main()