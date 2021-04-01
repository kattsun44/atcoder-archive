"""
*    author:  kattsun
*    created: 01-03-2021 21:16:20
"""

def main():
    n = int(input())
    t = list(map(int, input().split()))
    m = int(input())

    for i in range(m):
        p,x = map(int, input().split())
        t0 = t[:]
        t0[p-1] = x
        print(sum(t0))
    

if __name__ == '__main__':
    main()