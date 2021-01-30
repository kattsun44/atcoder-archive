"""
*    author:  kattsun
*    created: 23-01-2021 21:11:15
"""

def main():
    n = int(input())
    A = list(map(int, input().split(' ')))
    ans = 0

    for l in range(n):
        mini = A[l]
        for r in range(l, n):
            mini = min(mini, A[r])
            ans  = max(ans, (r-l+1)* mini)
    
    print(ans)

if __name__ == '__main__':
    main()