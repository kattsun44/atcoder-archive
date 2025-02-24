"""
*    author:  kattsun
*    created: 04-07-2021 20:04:37
"""

def main():
    N, M = map(int, input().split())
    if 1 * N <= M <= 6 * N:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()