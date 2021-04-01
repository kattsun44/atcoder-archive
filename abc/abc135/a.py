def main():
    a, b = list(map(int, input().split(' ')))
    ans = int((a + b) / 2) if (a + b) % 2 == 0 else 'IMPOSSIBLE'
    print(ans)

if __name__ == '__main__':
    main()