"""
*    author:  kattsun
*    created: 28-05-2021 08:57:27
"""


def main():
    A, B, N = map(int, input().split())
    if N < B:
        print(A*N//B)
    else:
        print(A*(B-1)//B)


if __name__ == '__main__':
    main()
