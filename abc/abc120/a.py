def main():
    a, b, c = list(map(int, input().split(' ')))
    
    if a * c <= b:
        print(c)
    else:
        print(int(b / a))


if __name__ == '__main__':
    main()