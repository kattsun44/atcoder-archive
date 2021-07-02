"""
*    author:  kattsun
*    created: 02-07-2021 07:51:26
"""

def main():
    H, W = map(int, input().split())
    if H != 1 and W != 1:
        print(-(-H//2) * -(-W//2))
    else:
        print(H*W)

if __name__ == '__main__':
    main()