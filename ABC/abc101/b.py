def main():
    n = int(input())
    str_n = str(n)
    s_n = 0

    for i in str_n:
        s_n += int(i)
    
    ans = 'Yes' if n % s_n == 0 else 'No'
    
    print(ans)

if __name__ == '__main__':
    main()