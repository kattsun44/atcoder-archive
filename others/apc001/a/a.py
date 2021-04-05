"""
*    author:  kattsun
*    created: 06-04-2021 07:39:55
"""

def main():
    x, y = map(int, input().split())
    if x % y == 0:
        print(-1)
    else:
        print(x)

if __name__ == '__main__':
    main()