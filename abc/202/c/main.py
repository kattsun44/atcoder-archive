"""
*    author:  kattsun
*    created: 22-05-2021 21:10:27
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    cnt = [0] * 1010100
    for j in range(N):
        cnt[B[C[j]-1]] += 1
    for i in range(N):
        ans += cnt[A[i]]
    print(ans)


if __name__ == '__main__':
    main()
