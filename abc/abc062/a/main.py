"""
*    author:  kattsun
*    created: 12-07-2021 08:47:09
"""

def main():
    x, y = map(int, input().split())
    z = {x,y}
    a = {1,3,5,7,8,10,12}
    b = {4,6,9,12}
    c = {2}
    if z & a == z or z & b == z or z & c == z:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()