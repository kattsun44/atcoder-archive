"""
*    author:  kattsun
*    created: 28-06-2021 11:21:44
"""

def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        ans += (N-1)//i
    print(ans)

if __name__ == '__main__':
    main()