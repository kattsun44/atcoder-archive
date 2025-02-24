def main():
    h, w, k = map(int, input().split(' '))
    board = []

    for i in range(h):
        board.append(input().strip())
    
    print(board)

if __name__ == '__main__':
    main()