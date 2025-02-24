"""
*    author:  kattsun
*    created: 11-06-2021 06:47:03
"""

def main():
    N, K = map(int, input().split())
    print(K*(K-1)**(N-1))

if __name__ == '__main__':
    main()