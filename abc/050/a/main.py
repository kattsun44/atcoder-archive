"""
*    author:  kattsun
*    created: 25-08-2021 13:14:13
"""

def main():
    N, op,  M = map(str, input().split())
    N = int(N)
    M = int(M)
    if op == '+':
        print(N+M)
    else:
        print(N-M)

if __name__ == '__main__':
    main()