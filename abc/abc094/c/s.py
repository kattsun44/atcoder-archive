"""
*    author:  kattsun
*    created: 18-05-2021 07:19:17
"""

def main():
    N = int(input())
    X = list(map(int, input().split()))
    X_sorted = sorted(X)
    m1 = X_sorted[len(X) // 2 - 1]
    m2 = X_sorted[len(X) // 2]
    for i in range(N):
      if X[i] <= m1:
        print(m2)
      else:
        print(m1)

if __name__ == '__main__':
    main()