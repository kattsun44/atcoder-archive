"""
*    author:  kattsun
*    created: 29-07-2021 06:38:44
"""

def main():
    H, W = map(int, input().split())
    A = []
    B = []
    for _ in range(H):
        row = list(map(int, input().split()))
        A.append(row)
    for i in range(H):
        row = list(map(int, input().split()))
        for j in range(W):
            A[i][j] -= row[j]

    cnt = 0
    for i in range(H-1):
        for j in range(W-1):
            num = -A[i][j] # 2x2マス見ていくときに、左上の数を引いていく
            A[i][j] += num
            A[i+1][j] += num
            A[i][j+1] += num
            A[i+1][j+1] += num
            cnt += abs(num) # 操作回数を記録

    judge = 0
    for i in range(H):
        judge += sum(A[i])
    if judge:
        print('No')
    else:
        print('Yes')
        print(cnt)


if __name__ == '__main__':
    main()