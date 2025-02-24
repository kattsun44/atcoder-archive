"""
*    author:  kattsun
*    created: 02-07-2021 07:18:42
"""

def main():
    A, B, C = map(int, input().split())
    divisor = 998244353
    print(A*(A+1)//2 * B*(B+1)//2 * C*(C+1)//2 % divisor)

if __name__ == '__main__':
    main()