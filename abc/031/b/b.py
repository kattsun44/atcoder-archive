"""
*    author:  kattsun
*    created: 28-02-2021 21:58:15
"""

def main():
    l,h = map(int, input().split())
    n = int(input())

    for i in range(n):
        a = int(input())
        if a < l:
            print(l-a)
        elif a > h:
            print(-1)
        else:
            print(0)

if __name__ == '__main__':
    main()