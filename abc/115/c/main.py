"""
*    author:  kattsun
*    created: 23-06-2021 09:36:50
"""

def main():
    N, K = map(int,input().split())
    trees = []
    for i in range(N):
        trees.append(int(input()))
    trees.sort()
    ans = float('inf')
    for i in range(N - K + 1):
        hmin = trees[i]
        hmax = trees[i+K-1]
        ans = min(ans, hmax-hmin)
    print(ans)

if __name__ == '__main__':
    main()