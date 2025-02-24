"""
*    author:  kattsun
*    created: 13-02-2021 21:11:05
"""
from math import factorial
def main():
    t = int(input())
    for i in range(t):
        c0, c1 = map(int, input().split())
        if c0 * 2 > c1:
            print(0)
        else:
            print(int((c1-c0*2+1)/2*(2+c1-c0*2)))

if __name__ == '__main__':
    main()