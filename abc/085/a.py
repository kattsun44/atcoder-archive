def main():
    Y, M, D = list(map(str.strip, input().split('/')))
    
    print('2018/' + M + '/' + D)

if __name__ == '__main__':
    main()