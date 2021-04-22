"""
*    author:  kattsun
*    created: 23-03-2021 18:51:48
"""


def main():
    s = input().strip()
    ans = 0
    cont = 0
    for i in range(len(s)):
        u = s[i]
        if i == 0:
            ans += 1
        else:
            if u == pre:
                cont += 1
                ans += cont + 1
            else:
                cont = 0
                if u == '<':
                    ans += 1
        pre = u

    print(ans)


if __name__ == '__main__':
    main()
