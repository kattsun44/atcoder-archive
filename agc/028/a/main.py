"""
*    author:  kattsun
*    created: 29-06-2021 07:19:07
"""
import math
def lcm(x,y):
    return (x*y)//math.gcd(x,y)
def main():
    N, M = map(int, input().split())
    S = input().strip()
    T = input().strip()

    G = math.gcd(N,M)
    L = lcm(N,M)

    for i in range(G):
        if S[i*N//G] != T[i*M//G]:
            print(-1)
            return

    print(L)

if __name__ == '__main__':
    main()