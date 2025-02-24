def main():
    a, b, c = list(input().split(' '))
    c = c.strip()
    l = [a, b, c]
    
    ans = 'No' if a == b == c or len(l) == len(set(l)) else 'Yes'
    print(ans)

if __name__ == '__main__':
    main()