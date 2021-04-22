"""
*    author:  kattsun
*    created: 22-04-2021 19:15:02
"""


def main():
    n = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    search = 1
    for a in A:
        if a == search:
            search += 1
        else:
            cnt += 1

    if n == cnt:
        print(-1)
    else:
        print(cnt)


if __name__ == '__main__':
    main()
