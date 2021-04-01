import math
def main():
    n, a, b = list(map(int, input().split(' ')))
    an = a * math.floor(n / (a + b))
    s = n % (a + b)
    
    if s > a:
        ans = an + a
    else:
        ans = an + s
        

    print(ans)

if __name__ == '__main__':
    main()