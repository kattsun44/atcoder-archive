def main():
    r, d, x2000 = list(map(int, input().split(' ')))
    ans = x2000
    for i in range(10):
        ans = r * ans - d
        print(ans)

if __name__ == '__main__':
    main()