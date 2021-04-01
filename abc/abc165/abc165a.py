def main():
    k = int(input())
    a, b = list(map(int, input().split(' ')))
    
    for i in range(b + 1):
        if i >= a:
            if i % k == 0:
                print('OK')
                return
    print('NG')

if __name__ == '__main__':
    main()