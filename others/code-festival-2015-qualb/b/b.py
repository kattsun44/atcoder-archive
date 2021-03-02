"""
*    author:  kattsun
*    created: 03-02-2021 19:41:25
"""

def main():
    n,m = list(map(int, input().split()))
    A = list(map(int, input().split()))
    cnt = dict()

    for i in range(n):
        if A[i] in cnt:
            cnt[A[i]] += 1
        else:
            cnt[A[i]] = 1
    
    mx = max(cnt.values())
    ans = '?' if mx * 2 <= n else [k for k, v in cnt.items() if v == mx][0]

    print(ans)

if __name__ == '__main__':
    main()