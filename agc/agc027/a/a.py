"""
*    author:  kattsun
*    created: 06-04-2021 07:44:57
"""

def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    rest = x

    for i in range(n):
        if a[i] <= rest:
            if i + 1 != n or a[i] == rest:
                cnt += 1
        rest -= a[i]

    print(cnt)

if __name__ == '__main__':
    main()