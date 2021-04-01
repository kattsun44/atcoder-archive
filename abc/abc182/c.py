import itertools
def main():
    n = list(map(int, list(input().strip())))
    ans = -1
    
    #すべてのn各桁の組合せを出力
    for i in range(1, len(n)+1):
        for j in itertools.combinations(n, i):
            s = sum(list(j))
            if s % 3 == 0 and len(list(j)) >= ans:
                ans = len(n) - len(list(j))
    
    print(ans)

if __name__ == '__main__':
    main()