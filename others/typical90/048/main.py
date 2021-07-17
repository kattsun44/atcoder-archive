"""
*    author:  kattsun
*    created: 17-07-2021 07:58:55
"""


def main():
    N, K = map(int, input().split())
    score = []
    for i in range(N):
        A, B = map(int, input().split())
        score.append(B)
        score.append(A-B)
    score.sort(reverse=True)
    ans = 0
    for i in range(K):
        ans += score[i]
    print(ans)


if __name__ == '__main__':
    main()
