def main():
    a, b = list(map(int, input().split(' ')))
    l = [a + b, a - b, a * b]
    
    print(max(l))

if __name__ == '__main__':
    main()