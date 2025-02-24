"""
*    author:  kattsun
*    created: 29-05-2021 09:26:03
"""


def main():
    L, R = map(int, input().split())
    loop = min(2019, R-L)
    ans = 2019
    for i in range(L, L+loop):
        for j in range(L+1, L+loop+1):
            ans = min(ans, (i*j) % 2019)
    print(ans)


if __name__ == '__main__':
    main()
