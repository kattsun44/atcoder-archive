def main():
    a, b = list(map(int, input().split(' ')))
    
    ans = 'Yes' if (a * b) % 2 == 1 else 'No'
    print(ans)

if __name__ == '__main__':
    main()