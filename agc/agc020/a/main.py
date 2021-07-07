"""
*    author:  kattsun
*    created: 07-07-2021 07:51:08
"""

def main():
    N, A, B = map(int, input().split())
    if (B - A) % 2 == 0:
        print('Alice')
    else:
        print('Borys')

if __name__ == '__main__':
    main()