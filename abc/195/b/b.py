"""
*    author:  kattsun
*    created: 14-03-2021 10:34:13
"""

def main():
    a,b,w = map(int, input().split())
    w *= 1000
    INF = float('inf')
    l = INF
    r = -INF

    for n in range(1,w+1):
        if a*n <= w and b*n >=w:
            l = min(l,n)
            r = max(r,n)
    
    if l == INF:
        print('UNSATISFIABLE')
    else:
        print(l,r)

if __name__ == '__main__':
    main()