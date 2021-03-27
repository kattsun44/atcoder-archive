"""
*    author:  kattsun
*    created: 27-03-2021 21:01:23
"""


def main():
    h, w, x, y = map(int, input().split())
    x -= 1
    y -= 1
    board = []
    ans = 1  # 現在地のマス
    for i in range(h):
        board.append(input().strip())

    n, e, s, ws = [-1, w, h, -1]
    # 北
    for i in range(x):
        if board[i][y] == '#':
            n = max(n, i)  # '#'のある座標
    # 東
    for i in range(w - y-1):
        if board[x][i + y + 1] == '#':
            e = min(e, i + y + 1)  # '#'のある座標
    # 南
    for i in range(h - x-1):
        if board[i + x + 1][y] == '#':
            s = min(s, i + x + 1)  # '#'のある座標
    # 西
    for i in range(y):
        if board[x][i] == '#':
            ws = max(ws, i)  # '#'のある座標

    ans += (y - ws - 1) + (x - n - 1) + (e - y - 1) + (s - x - 1)
    print(ans)


if __name__ == '__main__':
    main()
