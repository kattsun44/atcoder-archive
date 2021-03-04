"""
*    author:  kattsun
*    created: 02-02-2021 20:39:00
"""

def main():
    n = int(input())
    a = list(map(int, input().split()))
    S = set()
    cnt = 0

    for i in range(n):
        t = (i+1, a[i])
        tr = (t[1], t[0])
        if tr in S:
            cnt += 1
        S.add(t)
    
    print(cnt)

if __name__ == '__main__':
    main()