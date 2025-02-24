"""
*    author:  kattsun
*    created: 28-03-2021 21:51:49
"""


def main():
    s = input().strip()
    a = s.find('A')
    z = s.rfind('Z')

    print(z-a+1)


if __name__ == '__main__':
    main()
