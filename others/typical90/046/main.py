"""
*    author:  kattsun
*    created: 16-07-2021 08:29:10
"""

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    x = [0] * 46
    y = [0] * 46
    z = [0] * 46
    for i in range(N):
        x[A[i] % 46] += 1
        y[B[i] % 46] += 1
        z[C[i] % 46] += 1
    ans = 0
    for i in range(46):
        for j in range(46):
            for k in range(46):
                if (i + j + k) % 46 == 0:
                    ans += x[i] * y[j] * z[k]
    print(ans)

if __name__ == '__main__':
    main()