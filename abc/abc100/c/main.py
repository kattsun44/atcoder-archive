"""
*    author:  kattsun
*    created: 05-06-2021 11:47:20
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for ai in A:
        ans += format(ai, 'b')[::-1].find('1')
    print(ans)


if __name__ == '__main__':
    main()
