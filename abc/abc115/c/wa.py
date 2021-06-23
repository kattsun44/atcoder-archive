"""
*    author:  kattsun
*    created: 23-06-2021 08:23:05
"""

def main():
    N, K = map(int, input().split())

    # 木の高さ別のカウントリスト
    cnt = dict()
    for i in range(N):
        h = int(input())
        cnt[h] = cnt[h] +1 if h in cnt else 1
    cnt_list = list(cnt.items())
    cnt_list = sorted(cnt_list)

    ans = float('inf')
    for i in range(min(K,len(cnt_list))):
        hmin = cnt_list[i][0]
        hmax = 0
        num_decorated_tree = 0
        j = i

        # 飾った木の数がKを超えるまでループし、hmaxを求める
        while num_decorated_tree < K:
            num_decorated_tree += cnt_list[j][1]
            hmax = cnt_list[j][0]
            j += 1
        ans = min(ans,hmax-hmin)
    print(ans)

if __name__ == '__main__':
    main()