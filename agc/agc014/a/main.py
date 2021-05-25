"""
*    author:  kattsun
*    created: 25-05-2021 08:09:06
"""

def main():
    a, b, c = map(int, input().split())
    # 最初から奇数があれば0回
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        print(0)
        return
    ab = abs(a-b)
    bc = abs(b-c)
    ca = abs(c-a)
    # 各差異が同じなら無限回
    if ab == bc and bc == ca and ca == ab:
        print(-1)
        return
    # 2で割れる回数
    ab2 = format(ab, 'b')[::-1].find('1')
    bc2 = format(bc, 'b')[::-1].find('1')
    ca2 = format(ca, 'b')[::-1].find('1')
    cnt = []
    if ab2 > 0:
        cnt.append(ab2)
    if bc2 > 0:
        cnt.append(bc2)
    if ca2 > 0:
        cnt.append(ca2)

    print(min(cnt))


if __name__ == '__main__':
    main()