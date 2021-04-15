"""
*    author:  kattsun
*    created: 16-04-2021 08:11:42
"""

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = dict()
    ans = 0

    for a in A:
        if a in cnt:
            cnt[a] += 1
        else:
            cnt[a] = 1

    for X in range(min(A), max(A)+1):
        X_cnt = 0
        if X - 1 in cnt:
            X_cnt += cnt[X - 1]
        if X in cnt:
            X_cnt += cnt[X]
        if X + 1 in cnt:
            X_cnt += cnt[X + 1]
        ans = max(ans, X_cnt)

    print(ans)

if __name__ == '__main__':
    main()