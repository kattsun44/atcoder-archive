def main():
    k, x = list(map(int, input().split(' ')))
    ans = 'Yes' if k * 500 >= x else 'No'
    print(ans)

if __name__ == '__main__':
    main()