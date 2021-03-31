"""
*    author:  kattsun
*    created: 01-04-2021 07:38:01
"""

def main():
    h,w = map(int, input().split())
    ans = 0
    if h == 1 or w == 1:
        print(1)
    else:
        print(-((-h*w)//2))

if __name__ == '__main__':
    main()