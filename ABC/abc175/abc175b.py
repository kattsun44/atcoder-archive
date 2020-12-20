def main():
    n = int(input())
    l = list(map(int, input().split(' ')))
    cnt = 0
    
    for i in range(len(l)):
        l1 = l[0:i] + l[i + 1:]
        for j in range(len(l1)):
            l2 = l1[0:j] + l1[j + 1:]
            for k in range(len(l2)):
                es = [l[i], l1[j], l2[k]]
                print(es, max(es), sum(es))
                if len(es) == len(set(es)):
                    if (max(es) * 2 < sum(es)):
                        cnt += 1
            l1 = l1[1:]
            if len(l1) <= 3:
                break
        l = l[1:]
        if len(l) <= 3:
            break
    
    print(cnt)


if __name__ == '__main__':
    main()