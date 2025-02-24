def main():
    h = list(map(int, input().split(' ')))[0]
    m = sum(list(map(int, input().split(' '))))
    
    judge = 'Yes' if m >= h else 'No'
    print(judge)


if __name__ == '__main__':
    main()