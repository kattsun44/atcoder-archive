"""
*    author:  kattsun
*    created: 04-07-2021 21:13:10
"""

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    minimum = K // N
    sorted_A = sorted(A)
    id = sorted_A[K % N - 1]
    for a in A:
        if a <= id and K % N != 0:
            print(minimum + 1)
        else:
            print(minimum)

if __name__ == '__main__':
    main()