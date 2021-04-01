def main():
    cnt = 0
    r1 = list(map(int, input().split(' ')))
    r2 = list(map(int, input().split(' ')))
    r3 = list(map(int, input().split(' ')))
    n = int(input())
    board = [r1, r2, r3]

    for _ in range(n):
        a = int(input())
        for j in range(3):
            for k in range(3):
                if board[j][k] == a:
                    board[j][k] = 'o'

    for i in range(3):
        cnt += 1 if board[i][0] == board[i][1] == board[i][2] else 0
        cnt += 1 if board[0][i] == board[1][i] == board[2][i] else 0
    
    cnt += 1 if board[0][0] == board[1][1] == board[2][2] else 0
    cnt += 1 if board[0][2] == board[1][1] == board[2][0] else 0

    ans = 'Yes' if cnt >= 1 else 'No'
    print(ans)

if __name__ == '__main__':
    main()