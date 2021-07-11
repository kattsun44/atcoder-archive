"""
*    author:  kattsun
*    created: 10-07-2021 20:59:58
"""

def main():
    A, B = map(int, input().split())
    if A <= B:
        print(B-A+1)
    else:
        print(0)

if __name__ == '__main__':
    main()