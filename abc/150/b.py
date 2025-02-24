def main():
    n = int(input())
    s = input().strip()
    cnt = 0

    for i in range(n - 2):
        w = s[i:i+3]
        if w == 'ABC':
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()