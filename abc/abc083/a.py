def main():
    a,b,c,d = list(map(int, input().split(' ')))
    l = a+b
    r = c+d

    if l == r:
        print('Balanced')
    elif l > r:
        print('Left')
    else:
        print('Right')
    
if __name__ == '__main__':
    main()