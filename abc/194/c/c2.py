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

    comb = list(itertools.combinations(cnt.keys(),2))

    for i in range(len(comb)):
        x,y = comb[i]
        ans += (x-y)**2 * cnt[x] * cnt[y]

    print(ans)

if __name__ == '__main__':
    main()