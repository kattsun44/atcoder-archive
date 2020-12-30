def main():
    n = int(input())
    s = set()

    for i in range(n):
        s.add(int(input()))
    
    print(len(s))

if __name__ == '__main__':
    main()