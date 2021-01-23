import itertools
def main():
    n = int(input())
    d = list(range(1, n+1))
    d2 = []
    p = ''.join(input().split(' '))
    q = ''.join(input().split(' '))

    # 辞書作成
    d = list(itertools.permutations(d, n))
    for i in d:
        i = list(map(lambda x: str(x), i))
        i = ''.join(i)
        d2.append(i)

    # 辞書のインデックスの差の絶対値
    print(abs(d2.index(p) - d2.index(q)))

if __name__ == '__main__':
    main()