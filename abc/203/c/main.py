"""
*    author:  kattsun
*    created: 30-05-2021 21:07:56
"""


def main():
    N, K = map(int, input().split())
    ans = 0
    cnt = dict()
    for i in range(N):
        A, B = map(int, input().split())
        if A in cnt:
            cnt[A] += B
        else:
            cnt[A] = B
    cnt_sorted = sorted(cnt.items(), key=lambda x: x[0])
    point = 0
    for i in range(len(cnt_sorted)):
        k, v = cnt_sorted[i]
        ans += min(k-point, K)
        if K < k-point:
            print(ans)
            return
        K -= (k-point)
        K += v
        point = k
    print(ans + K)


if __name__ == '__main__':
    main()
