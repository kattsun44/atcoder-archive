"""
*    author:  kattsun
*    created: 15-06-2021 07:13:01
"""

def main():
    N, A, B = map(int, input().split())
    if A > B :
        print(0)
    elif A == B:
        print(1)
    else:
        if N == 1:
            print(0)
        else:
            print((B-A)*(N-2)+1)


if __name__ == '__main__':
    main()