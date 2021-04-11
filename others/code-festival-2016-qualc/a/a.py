"""
*    author:  kattsun
*    created: 11-04-2021 15:05:16
"""


def main():
    s = input().strip()

    if s.find('C') != -1:
        if s[s.find('C'):].find('F') != -1:
            print('Yes')
            return

    print('No')


if __name__ == '__main__':
    main()
