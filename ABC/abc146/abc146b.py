import string
atoz = string.ascii_uppercase
def main():
    ans = ''
    n = int(input())
    s = input().strip()
    
    for i in range(len(s)):
        ans += atoz[(atoz.index(s[i]) + n) % len(atoz)]
    
    print(ans)

if __name__ == '__main__':
    main()