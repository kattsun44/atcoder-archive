"""
*    author:  kattsun
*    created: 30-03-2021 06:41:53
"""

def main():
    a, b = map(int, input().split())
    if a > 0:
        print('Positive')
    elif a <= 0 and b >= 0:
        print('Zero')
    else:
        if (b - a) % 2 == 0:
            print('Negative')
        else:
            print('Positive')

if __name__ == '__main__':
    main()