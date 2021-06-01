"""
*    author:  kattsun
*    created: 02-06-2021 06:43:29
"""

def main():
    N, L = map(int, input().split())
    s = []
    for i in range(N):
        s.append(input().strip())
    s.sort()
    print(''.join(s))

if __name__ == '__main__':
    main()