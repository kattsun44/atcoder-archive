"""
*    author:  kattsun
*    created: 03-07-2021 15:27:39
"""


def main():
    N = int(input())
    S = input().strip()
    if S[0] != S[-1]:
        print(1)
        return
    else:
        s = S[0]
        cnt = 0
        for c in S:
            if s != c:
                cnt += 1
            else:
                cnt = 0
            # もし 先頭の文字以外の文字が連続する部分があれば2回で削除できる
            if cnt == 2:
                print(2)
                return
    print(-1)


if __name__ == '__main__':
    main()
