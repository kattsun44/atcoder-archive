"""
*    author:  kattsun
*    created: 29-05-2021 16:06:18
"""


def main():
    atoz = [chr(i) for i in range(97, 123)]  # 小文字
    N = int(input())
    name = ''

    while N > 26:
        name = name + atoz[N % 26 - 1]
        if N % 26 == 0:
            N = N // 26 - 1
        else:
            N //= 26
    name = name + atoz[N % 26 - 1]
    print(''.join(list(reversed(name))))


if __name__ == '__main__':
    main()
