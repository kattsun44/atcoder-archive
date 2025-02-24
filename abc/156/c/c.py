import math
def main():
    N = int(input())
    X = list(map(int, input().split(' ')))
    total = 0
    ans = 1000000000
    for i in range(max(X) + 1):
        for x in X:
            total += abs(i - x) ** 2
        if ans > total:
            ans = total
        total = 0
    
    print(ans)

if __name__ == '__main__':
    main()