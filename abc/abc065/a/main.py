"""
*    author:  kattsun
*    created: 30-06-2021 06:45:35
"""

def main():
    X, A, B = map(int, input().split())
    if A >= B:
        print('delicious')
    elif A + X >= B:
        print('safe')
    else:
        print('dangerous')

if __name__ == '__main__':
    main()