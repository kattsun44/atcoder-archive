def main():
    a = int(input())
    s = input().strip()
    ans = s if a >= 3200 else 'red'
    print(ans)

if __name__ == '__main__':
    main()