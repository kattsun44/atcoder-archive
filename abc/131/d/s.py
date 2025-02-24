"""
*    author:  kattsun
*    created: 21-05-2021 07:19:55
"""

def main():
    N = int(input())
    l = []
    for i in range(N):
        l.append(tuple(map(int, input().split())))
    l_sorted = sorted(l, key=lambda x: x[1])
    a = 0
    for i in range(N):
        a += l_sorted[i][0]
        if a > l_sorted[i][1]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()