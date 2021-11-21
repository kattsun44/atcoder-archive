"""
*    author:  kattsun
*    created: 21-11-2021 13:02:51
"""


def main():
    N, K, S = map(int, input().split())
    ans = []
    for i in range(N):
        if K > 0:
            ans.append(S)
            K -= 1
        else:
            if S == 1_000_000_000:
                ans.append(1)
            else:
                ans.append(S+1)
    print(" ".join(map(str, ans)))


if __name__ == '__main__':
    main()
