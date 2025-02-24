"""
*    author:  kattsun
*    created: 17-05-2021 06:47:42
"""

def main():
    A = list(map(int, input().split()))
    x = max(A)
    A.remove(max(A))
    x1 = -(-x // 2)
    x2 = x // 2
    print((x1 - x2) * A[0] * A[1])

if __name__ == '__main__':
    main()