"""
*    author:  kattsun
*    created: 22-05-2021 21:02:23
"""


def main():
    S = input().strip()
    ans = ''
    for i in range(1, len(S)+1):
        c = S[-i]
        if c == '9':
            ans += '6'
        elif c == '6':
            ans += '9'
        else:
            ans += c
    print(ans)


if __name__ == '__main__':
    main()
