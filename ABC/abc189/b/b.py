"""
*    author:  kattsun
*    created: 23-01-2021 21:03:42
"""

def main():
    n, x = map(int, input().split(' '))
    x *= 100
    alc = 0
    cnt = 0
    
    for i in range(n):
        v,p = map(int, input().split(' '))
        alc += v * p
        cnt += 1
        if alc > x:
            print(cnt)
            return
    print(-1)

if __name__ == '__main__':
    main()