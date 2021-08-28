"""
*    author:  kattsun
*    created: 28-08-2021 15:14:59
"""


def main():
    a1, a2, a3 = map(int, input().split())
    x = a1+a3
    y = a2*2
    if x <= y:
        print(y-x)
    else:
        if x % 2 == 1:
            print(1 + (x + 1 - y)//2)
        else:
            print((x-y)//2)


if __name__ == '__main__':
    main()
