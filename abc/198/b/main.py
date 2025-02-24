"""
*    author:  kattsun
*    created: 21-06-2021 08:15:40
"""

def main():
    N = list(map(str,input().strip()))
    for i in range(20):
        if N == list(reversed(N)):
            print('Yes')
            return
        N = ['0'] + N
    print('No')


if __name__ == '__main__':
    main()