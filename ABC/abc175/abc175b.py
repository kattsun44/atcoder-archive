def main():
    n = int(input())
    l = list(map(int, input().split(' ')))
    cnt = 0
    
    for i in range(len(l)):
        for j in range(i):
            for k in range(j):
                es = [l[i], l[j], l[k]] 
                if len(es) == len(set(es)):
                    if (max(es) * 2 < sum(es)):
                        cnt += 1
    
    print(cnt)


if __name__ == '__main__':
    main()