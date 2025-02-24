"""
*    author:  kattsun
*    created: 18-02-2021 07:36:52
"""

def main():
    board = []
    for i in range(3):
        board.append(list(map(int, input().split())))
    
    for i in range(2):
        s = set()
        for j in range(3):
            s.add(board[i][j] - board[i+1][j])
        if len(s) != 1:
            print('No')
            return
    
    print('Yes')

if __name__ == '__main__':
    main()