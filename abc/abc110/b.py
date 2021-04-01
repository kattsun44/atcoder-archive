def main():
    n, m, x, y = list(map(int, input().split(' ')))
    X = list(map(int, input().split(' ')))
    Y = list(map(int, input().split(' ')))
    if x < min(Y) and y > max(X) and max(X) < min(Y):
        print('No War')
    else:
        print('War')

if __name__ == '__main__':
    main()