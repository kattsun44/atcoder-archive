def main():
    a, b = list(map(int, input().split(' ')))
    
    if a < 6:
        print(0)
    elif 6 <= a <= 12:
        print(int(b / 2))
    else:
        print(b)

if __name__ == '__main__':
    main()