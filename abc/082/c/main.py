"""
*    author:  kattsun
*    created: 26-05-2021 06:52:50
"""

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = dict()
    ans = 0
    for i in range(N):
        if A[i] in cnt:
            cnt[A[i]] += 1
        else:
            cnt[A[i]] = 1
    cnt_sorted = sorted(cnt.items(), key= lambda x: x[0], reverse=True)
    for k, v in cnt_sorted:
        if k < v:
            ans += v - k
        elif k > v:
            ans += v
    print(ans)

if __name__ == '__main__':
    main()