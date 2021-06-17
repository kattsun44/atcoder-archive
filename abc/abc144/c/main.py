"""
*    author:  kattsun
*    created: 17-06-2021 08:06:17
"""


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    N = int(input())
    divs = make_divisors(N)
    if len(divs) % 2 == 0:
        a = divs[len(divs)//2-1]
        b = divs[len(divs)//2]
    else:
        a = divs[len(divs)//2]
        b = divs[len(divs)//2]
    print(a+b - 2)


if __name__ == '__main__':
    main()
