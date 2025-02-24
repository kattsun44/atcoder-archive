def main():
    s = input().strip()
    n = 0

    for i in s:
        n += 1 if i == '+' else -1
    
    print(n)

if __name__ == '__main__':
    main()