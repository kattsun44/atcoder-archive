"""
*    author:  kattsun
*    created: 17-03-2021 07:47:43
"""


def main():
    n = int(input())
    l = len(str(n))
    n0 = int(str(n)[0])
    if len(set(str(n)[1:])) == 1 and '9' in set(str(n)[1:]):
        print(n0 + 9*(l-1))
    else:
        print(n0-1+9*(l-1))


if __name__ == '__main__':
    main()
