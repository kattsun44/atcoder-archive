def main():
    n = int(input())
    t = 0

    for i in range(n):
        x, u = list(input().split(' '))
        x = float(x)
        t += x if u == 'JPY' else x * 380000
    
    print(t)

if __name__ == '__main__':
    main()