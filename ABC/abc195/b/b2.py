"""
*    author:  kattsun
*    created: 14-03-2021 10:53:33
"""

def main():
    a,b,w = map(int, input().split())
    w *= 1000
    l = w//b
    r = -(-w//a)
    if l == r:
        print('UNSATISFIABLE')
    else:
        print(l,r)

if __name__ == '__main__':
    main()