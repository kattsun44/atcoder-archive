def main():
    H, W = list(map(int, input().split(' ')))
    h, w = list(map(int, input().split(' ')))
    
    print((H - h) * (W - w))

if __name__ == '__main__':
    main()