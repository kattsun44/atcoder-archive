def main():
    n = int(input())
    l = list(map(int, input().split(' ')))
    ao = sorted(l)
    cnt = 0
    
    for i in range(n):
        if l[i] != ao[i]:
            cnt += 1
    
    if cnt <= 2:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()