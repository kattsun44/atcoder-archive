"""
*    author:  kattsun
*    created: 10-07-2021 21:01:08
"""

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) - N//2 <= X:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()