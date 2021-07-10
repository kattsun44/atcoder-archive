"""
*    author:  kattsun
*    created: 10-07-2021 11:09:30
"""


def main():
    N = int(input())
    A, B, C = list(map(int, input().split()))
    ans = float('inf')
    for i in range(10000):
        for j in range(10000-i):
            rem = N - (A * i + B * j)
            if rem >= 0 and rem % C == 0:
                k = rem // C
                ans = min(ans, i+j+k)
    print(ans)


if __name__ == '__main__':
    main()
