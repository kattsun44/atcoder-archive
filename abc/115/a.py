def main():
    d = int(input())
    ans = 'Christmas'
    
    for i in range(25 - d):
        ans += ' Eve'
    print(ans)

if __name__ == '__main__':
    main()