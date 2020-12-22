def main():
    n = input().split('\n')
    n = n[0]
    p1 = n[len(n) - 1]
    c = 'hon'
    pon = ['0', '1', '6', '8']

    if p1 == '3':
        c = 'bon'
    elif p1 in pon:
        c = 'pon'

    print(c)

if __name__ == '__main__':
    main()