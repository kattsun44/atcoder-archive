"""
*    author:  kattsun
*    created: 17-08-2021 07:34:41
"""

def main():
    H, W = map(int, input().split())
    board = []
    for i in range(H):
        S = input().strip() + '#'
        board.append(S)
    board.append('#' * (W + 1))

    cnt = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] == '.':
                if board[i][j+1] == '.':
                    cnt += 1
                if board[i+1][j] == '.':
                    cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()