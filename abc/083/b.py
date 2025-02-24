def main():
    n, a, b = list(map(int, input().split(' ')))
    ans = 0
    
    for i in range(n):
        each_digits = list(map(int, list(str(i + 1))))
        each_digits_sum = sum(each_digits)
        if a <= each_digits_sum <= b:
            ans += i + 1

    print(ans)

if __name__ == '__main__':
    main()