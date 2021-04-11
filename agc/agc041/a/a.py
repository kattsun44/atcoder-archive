"""
*    author:  kattsun
*    created: 12-04-2021 06:50:06
"""

def main():
    N, A, B = map(int, input().split())
    if (B - A) % 2 == 0:
        print(int((B - A) // 2))
    else:
        print(min(A - 1, N - B)+ 1 + int((B - A - 1)//2))

if __name__ == '__main__':
    main()