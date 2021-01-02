def main():
    n = int(input())
    
    for i in range(9):
        for j in range(9):
            if n == (i + 1) * (j + 1):
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()