"""
*    author:  kattsun
*    created: 16-01-2021 16:57:30
"""

def main():
    n = int(input())
    total = 0

    for i in range(n):
       l,r = map(int, input().split(' '))
       total += r-l+1
    
    print(total)

if __name__ == '__main__':
    main()