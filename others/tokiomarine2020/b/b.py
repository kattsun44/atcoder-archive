"""
*    author:  kattsun
*    created: 08-04-2021 07:56:13
"""

def main():
    A, V = map(int, input().split())
    B, W = map(int, input().split())
    T = int(input())

    pos_diff = abs(A-B)
    vel_diff = V - W

    if vel_diff * T >= pos_diff:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()