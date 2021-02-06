"""
*    author:  kattsun
*    created: 05-02-2021 21:02:14
"""

def main():
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    for i in range(n-1):
        total += a[i+1] - a[i]
    
    print(total/(n-1))

if __name__ == '__main__':
    main()