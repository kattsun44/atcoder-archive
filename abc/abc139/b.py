def main():
    a, b = list(map(int, input().split(' ')))
    cnt, t = [0, 0]

    while b != 1 and t < b:
        cnt += 1
        t += a - 1 if cnt != 1 else a
        pass
    
    print(cnt)

if __name__ == '__main__':
    main()