def main():
    n = int(input())
    a = int(input())
    ans = 'Yes' if n % 500 <= a else 'No'
    print(ans)

if __name__ == '__main__':
    main()