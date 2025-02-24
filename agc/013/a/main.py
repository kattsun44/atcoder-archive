"""
*    author:  kattsun
*    created: 02-06-2021 07:02:23
"""

def main():
    N = int(input())
    A = list(map(int, input().split()))
    trend = ''
    ans = 1
    for i in range(N-1):
        if A[i] < A[i + 1]:
            if trend == '':
                trend = 'inc'
            elif trend == 'dec':
                ans += 1
                trend = ''
        elif A[i] > A[i+1]:
            if trend == '':
                trend = 'dec'
            elif trend == 'inc':
                ans += 1
                trend = ''
    print(ans)

if __name__ == '__main__':
    main()