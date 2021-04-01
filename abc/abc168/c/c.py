"""
*    author:  kattsun
*    created: 31-03-2021 18:53:54
"""
from math import cos, sqrt, radians


def main():
    A, B, H, M = map(int, input().split())
    h = (H * 30 + M * 0.5)
    m = M * 6
    theta = abs(h - m)
    ans = sqrt(A ** 2 + B ** 2 - 2 * A * B * cos(radians(theta)))

    print(ans)


if __name__ == '__main__':
    main()
