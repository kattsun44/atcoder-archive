"""
*    author:  kattsun
*    created: 24-04-2021 21:03:13
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = max(A)
    b = min(B)
    if a > b:
        print(0)
    else:
        print(b - a + 1)


if __name__ == '__main__':
    main()
