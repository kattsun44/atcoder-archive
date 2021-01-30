def main():
    n = input().strip()
    ans = ''

    for i in n:
        ans += '9' if i == '1' else '1'
    
    print(int(ans))

if __name__ == '__main__':
    main()