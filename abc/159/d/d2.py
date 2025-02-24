"""
*    author:  kattsun
*    created: 08-02-2021 21:07:49
"""
from math import factorial
def choose2(n):
    return int(n*(n-1)/2)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = dict()
    for i in range(n):
        if a[i] in cnt:
            cnt[a[i]] += 1
        else:
            cnt[a[i]] = 1
    
    # 何も操作しないときの2個の選び方総数
    total = 0
    for v in cnt.values():
        if v >= 2:
            total += choose2(v)
    for i in range(n):
        ans = total

        # total から C(a[i], 2) だけ減って C(a[i]+1, 2) だけ増えたとみなせる
        ans -= choose2(cnt[a[i]])
        ans += choose2(cnt[a[i]]-1)
        print(ans)

if __name__ == '__main__':
    main()