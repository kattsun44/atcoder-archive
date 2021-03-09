"""
*    author:  kattsun
*    created: 09-03-2021 20:02:10
"""

def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = []

    for i in range(n):
        l.append((i+1,a[i]))
    
    l = sorted(l, key = lambda x:x[1])
    l = [i[0] for i in l]
    print(' '.join(map(str,l)))
    
    # for i in range(n):
    #     print(l[0])

if __name__ == '__main__':
    main()