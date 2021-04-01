def main():
    N, K = map(int, input().split(' '))
    H = list(map(int, input().split(' ')))
    H = sorted(H)

    if len(H) <= K:
        print(0)
        return
    else:
        print(sum(H[:len(H) - K]))

if __name__ == '__main__':
    main()