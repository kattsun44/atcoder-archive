def main():
    a, b = list(map(int, input().split(' ')))
    
    ans = 'Yay!' if a <= 8 and b <= 8 else ':('
    print(ans)

if __name__ == '__main__':
    main()