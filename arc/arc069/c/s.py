"""
*    author:  kattsun
*    created: 18-05-2021 06:51:34
"""

def main():
    N, M = map(int, input().split())
    print(min((N * 2 + M) // 4, M // 2))

if __name__ == '__main__':
    main()