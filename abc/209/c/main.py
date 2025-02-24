"""
*    author:  kattsun
*    created: 10-07-2021 21:03:24
"""

def main():
    div = 1000000000 + 7
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans *= (C[i] - i)
        ans = ans % div
    print(ans)

if __name__ == '__main__':
    main()