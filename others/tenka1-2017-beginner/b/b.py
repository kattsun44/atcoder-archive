"""
*    author:  kattsun
*    created: 20-03-2021 08:18:14
"""


def main():
    n = int(input())
    A = []
    B = []
    ans = 0
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 「Aの最小値-1」「Aの最大値と最小値の差+1」「Bの最小値」の和が答え
    ans = (min(A) - 1) + (max(A) - min(A) + 1) + min(B)

    print(ans)


if __name__ == '__main__':
    main()
