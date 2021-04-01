"""
*    author:  kattsun
*    created: 07-03-2021 10:26:18
"""
import itertools

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = {}
    ans = 0
    for i in range(n):
        if a[i] in cnt:
            cnt[a[i]] += 1
        else:
            cnt[a[i]] = 1

    keys = list(cnt.keys())

    for key1 in keys:
        for key2 in keys:
            ans += (key1-key2)**2 * cnt[key1] * cnt[key2]
    print(int(ans/2))

if __name__ == '__main__':
    main()