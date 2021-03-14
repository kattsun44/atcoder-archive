"""
*    author:  kattsun
*    created: 14-03-2021 16:37:22
"""
import itertools
import functools


def main():
    n = int(input())
    A = list(map(int, input().split()))
    cnt = 0

    # 2次元リスト作成
    l = []
    for a in A:
        l.append([a-1, a, a+1])

    # 直積リスト作成
    ll = list(itertools.product(*l))

    for i in range(len(ll)):
        # 総積を計算しtpに代入
        tp = functools.reduce(lambda x, y: x*y, ll[i])
        if tp % 2 == 0:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
