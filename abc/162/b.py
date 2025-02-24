def main():
    n = int(input())
    total = 0

    for i in range(n):
        if (i + 1) % 3 != 0 and (i + 1) % 5 != 0:
            total += i + 1
    
    print(total)

if __name__ == '__main__':
    main()