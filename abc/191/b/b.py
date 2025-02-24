"""
*    author:  kattsun
*    created: 06-02-2021 21:04:15
"""

def main():
    n,x = map(int, input().split())
    A = list(map(int, input().split()))
    B = []

    for a in A:
        if a != x:
            B.append(a)
    
    print(" ".join([str(i) for i in B]))

if __name__ == '__main__':
    main()