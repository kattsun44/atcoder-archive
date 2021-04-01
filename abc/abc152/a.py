def main():
    n, m = list(map(int, input().split(' ')))
    
    jdg = 'Yes' if n == m else 'No'
    print(jdg)

if __name__ == '__main__':
    main()