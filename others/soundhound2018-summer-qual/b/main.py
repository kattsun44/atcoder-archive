"""
*    author:  kattsun
*    created: 08-07-2021 08:15:48
"""


def main():
    S = input().strip()
    w = int(input())
    ans = ''
    for i in range(len(S)):
        if i % w == 0:
            ans = ans + S[i]
    print(ans)


if __name__ == '__main__':
    main()
