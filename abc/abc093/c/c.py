"""
*    author:  kattsun
*    created: 15-02-2021 21:37:18
"""
from math import ceil
def main():
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    while True:
        if a[0] == a[1]:
            cnt += a[2] - a[0]
            print(cnt)
            return
        elif a[1] == a[2]:
            if (a[2] - a[0]) % 2 == 0:
                cnt += ceil((a[2] - a[0]) / 2) 
            else:
                cnt += ceil((a[2] - a[0]) / 2) + 1
            print(cnt)
            return
        a[a.index(min(a))] += 2
        a.sort()
        cnt += 1

if __name__ == '__main__':
    main()