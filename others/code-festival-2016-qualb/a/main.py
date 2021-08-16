"""
*    author:  kattsun
*    created: 15-08-2021 20:03:32
"""


def main():
    S = input().strip()
    W = "CODEFESTIVAL2016"
    ans = 0
    for i in range(len(S)):
        if S[i] != W[i]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
