def main():
    a, b = list(map(str.strip, input().split(' ')))
    a= list(map(int, list(a)))
    b= list(map(int, list(b)))
    
    
    print(max(sum(a), sum(b)))

if __name__ == '__main__':
    main()