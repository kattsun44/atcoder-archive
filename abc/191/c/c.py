"""
*    author:  kattsun
*    created: 06-02-2021 21:13:38
"""

def main():
    h,w = list(map(int, input().split()))
    ans = 0
    board = []
    for i in range(h):
        board.append(input().strip())
    
    for i in range(h-2):
        for j in range(w-2):
            point = board[i+1][j+1]
            if point == '#':
                a = [board[i][j], board[i][j+1], board[i][j+2], board[i+1][j]]
                if a.count('#') == 4:
                    ans += 0
                elif a.count('#') == 0:
                    ans += 4
                elif a[1] == a[3] == '.':
                    ans += 4
                elif a[1] == a[3] == '#':
                    ans -= 2
                elif a[1] == '#':
                    if a.count('#') == 2:
                        ans += 2
                    elif a.count('#') == 3:
                        ans += 4
                elif a[3] == '#':
                    if a[0] == '#':
                        ans += 2

    
    print(ans)

if __name__ == '__main__':
    main()