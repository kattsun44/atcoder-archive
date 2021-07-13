"""
*    author:  kattsun
*    created: 13-07-2021 22:15:54
"""
import math


def main():
    T = int(input())
    L, X, Y = map(int, input().split())
    Q = int(input())
    for i in range(Q):
        E = int(input())
        x = 0
        y = -L/2 * math.sin(math.radians(360 * E/T))
        z = L/2 - L/2 * math.cos(math.radians(360 * E/T))
        A = math.sqrt(X**2 + (y-Y)**2)
        B = z
        print(math.degrees(math.atan2(B, A)))


if __name__ == '__main__':
    main()
