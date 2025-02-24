"""
*    author:  kattsun
*    created: 11-05-2021 08:47:33
"""

def main():
    H = int(input())
    N = 1
    while N * 2 <= H:
        N *= 2
    print(N * 2 - 1)

if __name__ == '__main__':
    main()