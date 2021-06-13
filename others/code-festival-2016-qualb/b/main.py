"""
*    author:  kattsun
*    created: 12-06-2021 18:24:32
"""


def main():
    N, A, B = map(int, input().split())
    S = input().strip()
    cnt = 0
    cnt_b = 0
    for i in range(N):
        if S[i] == 'a':
            if cnt < A+B:
                print('Yes')
            else:
                print('No')
            cnt += 1
        elif S[i] == 'b':
            if cnt < A+B and cnt_b < B:
                print('Yes')
                cnt += 1
            else:
                print('No')
            cnt_b += 1
        else:
            print('No')
        # print(cnt, cnt_b)


if __name__ == '__main__':
    main()
