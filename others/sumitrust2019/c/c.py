"""
*    author:  kattsun
*    created: 02-04-2021 07:43:04
"""

def main():
    x = int(input())

    # 十の位までの数値
    rest = x % 100

    # 下2桁がrestと等しくなるときの最小値
    total = 0

    # 5から1までループ
    for i in range(5, 0, -1):
        # i が何個入るか
        cnt = rest // i
        # totalを更新
        total += cnt * (100 + i)
        # 余りを更新
        rest = rest % i

    # totalがxより小さければOK
    if total <= x:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()