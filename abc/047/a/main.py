"""
*    author:  kattsun
*    created: 06-07-2021 06:59:56
"""

def main():
    a, b, c = map(int, input().split())
    if a+b==c or b+c==a or c+a==b:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()