"""
*    author:  kattsun
*    created: 09-05-2021 11:06:24
"""


def main():
    S = input().strip()
    cnt = {'<': 0, '>': 0}
    prev = S[0]
    ans = 0
    for c in S:
        # 記号が変わる場合の処理
        if c != prev:
            if c == '<':
                # 直前までの記号の数に応じた数を足す
                ans += cnt['>'] * (cnt['>'] - 1) // 2
                # < と > のカウント数のうち大きい方を足す
                ans += max(cnt['<'], cnt['>'])
                # カウント数リセット
                cnt['<'], cnt['>'] = 0, 0
            else:
                # 直前までの記号の数に応じた数を足す
                ans += cnt['<'] * (cnt['<'] - 1) // 2
        cnt[c] += 1
        prev = c
    # 最後の操作
    cnt[c] += 1
    ans += cnt[c] * (cnt[c] - 1) // 2

    print(ans)


if __name__ == '__main__':
    main()
