import math
def main():
    x, k, d = list(map(int, input().split(' ')))
    x = abs(x)
    ans = 0
    
    if x >= k * d:
        print(x - k * d)
        return
    else:
        e = math.floor(x / d)
        k = k - e
        ans = x - e * d
        if k % 2 != 0:
            ans = abs(ans - d)

    print(ans)

if __name__ == '__main__':
    main()