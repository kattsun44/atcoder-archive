def main():
    n, m = map(int, input().split(' '))
    idx = list(range(1, n + 1))
    H = list(map(lambda x:(next(iter(idx)), int(x)), input().split(' ')))
    
    print(H, idx)

if __name__ == '__main__':
    main()