"""
*    author:  kattsun
*    created: 22-03-2021 12:29:14
"""

def main():
    n = int(input())
    s = input().strip()
    x = 0
    ans = 0
    for i in range(n):
        if s[i] == 'I':
            x += 1
        else:
            x -= 1
        ans = max(ans,x)
    
    print(ans)

if __name__ == '__main__':
    main()