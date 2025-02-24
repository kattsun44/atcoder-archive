def main():
    x, y = list(map(int, input().split(' ')))
    ans = 'Yes' if abs(x - y) < 3 else 'No'
    print(ans)

if __name__ == '__main__':
    main()