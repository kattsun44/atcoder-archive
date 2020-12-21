import math
def main():
    n, d = list(map(int, input().split(' ')))
    cnt = 0
    
    for i in range(n):
        x, y = list(map(int, input().split(' ')))
        d_ = math.sqrt(x ** 2 + y ** 2)
        if d_ <= d:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()