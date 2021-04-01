def main():
    n = int(input())
    cnt = 0
    three = False

    for _ in range(n):
        a, b = list(map(int, input().split(' ')))
        if a == b:
            cnt += 1
            if cnt >= 3:
                three = True
        else:
            cnt = 0
    
    if three:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()