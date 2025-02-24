"""
*    author:  kattsun
*    created: 08-02-2021 20:08:22
"""
from math import factorial, floor
def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = {}
    for i in range(n):
        if a[i] in cnt:
            cnt[a[i]] += 1
        else:
            cnt[a[i]] = 1

    # 答えをメモ
    memo = dict(zip(list(set(a)), [0] * len(a)))

    for i in range(n):

        # i がすでに出ていたらメモから答えを出す
        if memo[a[i]] > 0:
            print(memo[a[i]])
            continue

        ans = 0
        
        cnt[a[i]] -= 1 # i番目の数字の個数をへらす

        # 残りの数から2個ずつ取る組合せ
        for j in cnt.values():
            if j >= 2:
                ans += int(factorial(j) / (factorial(2) * factorial(j - 2) ))
        print(ans)

        cnt[a[i]] += 1 # もとに戻す操作
        memo[a[i]] += ans # 答えをメモ


if __name__ == '__main__':
    main()