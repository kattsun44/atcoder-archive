"""
*    author:  kattsun
*    created: 29-04-2021 18:04:58
"""


def main():
    S = input().strip()
    cnt1 = 0
    cnt2 = 0
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == '0':
                cnt1 += 1
            else:
                cnt2 += 1
        else:
            if S[i] == '0':
                cnt2 += 1
            else:
                cnt1 += 1

    print(min(cnt1, cnt2))


if __name__ == '__main__':
    main()
