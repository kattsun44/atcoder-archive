"""
*    author:  kattsun
*    created: 21-06-2021 07:42:59
"""

def main():
    H, W = map(int, input().split())
    board = []
    V_total = [0] * W
    H_total = []
    for i in range(H):
        A = list(map(int, input().split()))
        board.append(A)
        for j in range(W):
            V_total[j] += A[j]
        H_total.append(sum(A))
    ans = []
    for i in range(H):
        row = []
        for j in range(W):
            row.append(V_total[j] + H_total[i] - board[i][j])
        ans.append(row)
    for i in range(H):
        print(' '.join(map(str, ans[i])))


if __name__ == '__main__':
    main()