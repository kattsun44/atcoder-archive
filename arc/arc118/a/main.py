"""
*    author:  kattsun
*    created: 03-06-2021 09:28:12
"""


def main():
    t, N = map(int, input().split())
    A = -(-100*N//t)
    ans = (100+t)*A//100-1
    print(ans)


if __name__ == '__main__':
    main()
