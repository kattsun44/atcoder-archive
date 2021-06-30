"""
*    author:  kattsun
*    created: 01-07-2021 08:25:01
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    avg = sum(A)/N
    diffs = []
    for i in range(N):
        diffs.append(abs(A[i]-avg))
    print(diffs.index(min(diffs)))


if __name__ == '__main__':
    main()
