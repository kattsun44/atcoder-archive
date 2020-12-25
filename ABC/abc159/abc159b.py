def main():
    n = input()
    n1 = n[:int((len(n) - 1) / 2)]
    n2 = n[int((len(n) + 3) / 2) - 1:]

    # n2入れ替えのため文字列をリスト化
    n1 = list(n1)
    n2 = list(n2)
    n2r = list(n2)
    n2r.reverse()

    if n1 == n2 and n1 == n2r:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()