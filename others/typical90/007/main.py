"""
*    author:  kattsun
*    created: 10-07-2021 09:23:29
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    # 一つ前を参照する場合とWhileで行き過ぎる場合があるので、リストの前後に inf を追加
    A = [float('inf')] + sorted(A) + [float('inf')]

    B = []
    B_dict = dict()  # Bの要素をキー、abs(a-b) を値に持つ辞書
    for i in range(Q):
        b = int(input())
        B.append(b)
        B_dict[b] = 1
    sorted_B = sorted(B)

    cursor = 1
    for i in range(Q):
        # AがBを超えるまでカーソルを動かす
        while(sorted_B[i] > A[cursor]):
            cursor += 1
        # カーソルが指しているAの要素と一つ前のAの要素との絶対値の差のうち、小さい方を適用する
        B_dict[sorted_B[i]] = min(
            abs(sorted_B[i] - A[cursor]), abs(sorted_B[i] - A[cursor-1]))

    for i in range(Q):
        # 本来の順番で出力
        print(B_dict[B[i]])


if __name__ == '__main__':
    main()
