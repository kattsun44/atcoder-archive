"""
*    author:  kattsun
*    created: 22-02-2021 20:19:59
"""

def main():
    n = int(input())
    s = input().strip()
    t = input().strip()
    ans = n * 2

    for i in range(n):
        if s[-(i+1):] == t[:i+1]:
            ans = n*2 - (i+1)
    
    print(ans)

if __name__ == '__main__':
    main()