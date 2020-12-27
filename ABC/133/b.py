import math
def main():
    n, d = list(map(int, input().split(' ')))
    X = []
    cnt = 0
    
    for i in range(n):
        X.append(list(map(int, input().split(' '))))
    
    for i in range(n):
        for j in range(n - i - 1):
            dt = 0
            for k in range(d):
                dt += (X[i][k] - X[j + 1 + i][k]) ** 2
            if math.sqrt(dt).is_integer():
                cnt += 1
    
    print(cnt)

if __name__ == '__main__':
    main()