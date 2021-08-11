"""
*    author:  kattsun
*    created: 10-08-2021 23:23:24
"""


def main():
    N = int(input())
    A = input().strip()
    B = input().strip()
    C = input().strip()
    ans = 0
    for i in range(N):
        tmp = len(set(A[i]+B[i]+C[i]))
        if tmp == 1:
            ans += 0
        elif tmp == 2:
            ans += 1
        else:
            ans += 2
    print(ans)


if __name__ == '__main__':
    main()
