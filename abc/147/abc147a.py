def main():
    t = sum(list(map(int, input().split(' '))))
    ans = 'bust' if t >= 22 else 'win'
    print(ans)

if __name__ == '__main__':
    main()