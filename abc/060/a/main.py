"""
*    author:  kattsun
*    created: 27-07-2021 22:29:39
"""

def main():
    A, B, C = map(str, input().split())
    if A[-1] == B[0] and B[-1] == C[0]:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()