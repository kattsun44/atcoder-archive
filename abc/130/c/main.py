"""
*    author:  kattsun
*    created: 18-06-2021 07:52:55
"""

def main():
    W, H, x, y = map(int, input().split())
    S = W*H/2
    is_m = 1 if x == W/2 and y == H/2 else 0
    print(S, is_m)

if __name__ == '__main__':
    main()