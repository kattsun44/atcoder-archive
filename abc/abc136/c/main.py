"""
*    author:  kattsun
*    created: 22-06-2021 07:15:51
"""

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = -1
    for i in range(1, N):
        max_h = max(H[i], max_h)
        if H[i] < H[i-1]:
            if max_h - H[i] >= 2:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()