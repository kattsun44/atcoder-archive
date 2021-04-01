"""
*    author:  kattsun
*    created: 16-01-2021 17:15:24
"""

def main():
    s = input().strip()
    ans = ""

    for i in range(len(s)):
        if i % 2 == 0:
            ans += s[i]
    
    print(ans)

if __name__ == '__main__':
    main()