"""
*    author:  kattsun
*    created: 05-03-2021 23:51:03
"""

def main():
    n = int(input())
    s = list(str(n))

    if s[0] == s[2]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()