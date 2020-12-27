def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    L = [a, b, c, d, e]
    ans = 'Yay!' if (max(L) - min(L)) <= k else ':('
    
    print(ans)

if __name__ == '__main__':
    main()