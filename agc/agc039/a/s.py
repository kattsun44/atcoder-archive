"""
*    author:  kattsun
*    created: 28-04-2021 07:40:03
"""

def main():
    S = input().strip()
    K = int(input())

    # 文字カウントを保持するリスト
    L = []
    # 入れ替え数を保持するリスト
    L_swap = []

    # 前の文字
    prev = ''
    for check in S:
        # 初期化
        if prev == '':
            L.append(1)
            L_swap.append(0)
        # 前の文字と同じ時
        elif prev == check:
            L[-1] += 1
            L_swap[-1] = L[-1] // 2
        # 異なればcnt//2をtotalに足す
        else:
            # リストにカウント個数を記録
            L.append(1)
            L_swap.append(0)
            # 新しい文字のカウントは1から
        prev = check

    # 入れ替え回数
    total = sum(L_swap)

    # 先頭と末尾の文字が異なれば、totalをK倍したものが答え
    if S[0] != S[-1]:
        print(total * K)
    # リストの長さが1=全部同じ文字の場合、文字列の長さ×K//2が答え
    elif len(L) == 1:
        print(len(S) * K // 2)
    # それ以外で先頭と末尾が同じ文字の場合
    else:
        ans = 0
        ans += L_swap[0] + L_swap[-1]
        ans += (L[0] + L[-1]) // 2 * (K - 1)
        ans += sum(L_swap[1:-1]) * K
        print(ans)

if __name__ == '__main__':
    main()