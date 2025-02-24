"""
*    author:  kattsun
*    created: 04-06-2021 08:17:18
"""

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if N >= M:
        print(0)
        return
    L = []
    for i in range(M-1):
        L.append(A[i+1]-A[i])
    L.sort()
    print(sum(L[:M-N]))

if __name__ == '__main__':
    main()