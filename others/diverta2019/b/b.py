"""
*    author:  kattsun
*    created: 03-03-2021 07:52:54
"""

def main():
    r,g,b,n = map(int, input().split())
    cnt = 0

    for i in range(0,n+1):
        for j in range(0,n+1-i):
            z = (n-(i*r+j*g))/b
            if z >= 0 and z == int(z):
                cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()