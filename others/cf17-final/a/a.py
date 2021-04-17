"""
*    author:  kattsun
*    created: 17-04-2021 09:20:22
"""


def main():
    s = input().strip()

    if 'KIH' in s:
        if 'AA' not in s:
            if s.replace('A', '') == 'KIHBR':
                print('YES')
                return

    print('NO')


if __name__ == '__main__':
    main()
