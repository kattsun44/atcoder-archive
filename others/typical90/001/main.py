"""
*    author:  kattsun
*    created: 04-08-2021 12:54:19
"""


def main():
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))

    # 貪欲法
    def check(M):
        cnt = 0
        pre = 0
        for a in A:
            if a - pre >= M and L - a >= M:
                cnt += 1
                pre = a
        if cnt >= K:
            return True
        else:
            return False

    _range = (0, L+1)
    while _range[1] - _range[0] > 1:
        candidate = sum(_range) // 2
        if check(candidate):
            _range = (candidate, _range[1])
        else:
            _range = (_range[0], candidate)
    print(_range[0])


if __name__ == '__main__':
    main()
