"""
*    author:  kattsun
*    created: 15-03-2021 17:08:16
"""
import collections


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c = collections.Counter(a)
    v = list(c.values())
    v.sort()
    m = len(set(a)) - k
    ans = 0
    for i in range(m):
        ans += v[i]

    print(ans)


if __name__ == '__main__':
    main()
