def main():
    s = input().strip()
    acgt = ['A', 'C', 'G', 'T']
    cnt = 0
    ans = 0

    for i in s:
        if i in acgt:
            cnt += 1
            if cnt > ans:
                ans = cnt
        else:
            cnt = 0
    
    print(ans)

if __name__ == '__main__':
    main()