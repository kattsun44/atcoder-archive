"""
*    author:  kattsun
*    created: 20-07-2021 07:17:02
"""


def main():
    N = int(input())
    S = input().strip() + '.'  # インデックスエラーを防ぐためのピリオド
    ans = 0
    now, prev = '', ''  # 今見ている文字、前に見た文字
    for i in range(N-1):
        now = S[i]

        # 前に見た文字と同じなら、前回のカウント結果を流用する
        if now == prev:
            ans += cnt
            continue

        # 今の文字以降の文字を走査する
        j = i
        while now == S[j]:
            j += 1
        cnt = N - j
        ans += cnt
        prev = now

    print(ans)


if __name__ == '__main__':
    main()
