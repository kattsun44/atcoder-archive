"""
*    author:  kattsun
*    created: 14-07-2021 06:55:13
"""
import math
def main():
    a, b, c = map(int, input().split())
    if a < c**b:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()