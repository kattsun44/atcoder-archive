"""
*    author:  kattsun
*    created: 20-02-2021 08:40:01
"""

def main():
    s = input().strip()
    ans = ""

    for c in s:
        if c == 'B':
            if len(c) > 0:
                ans = ans[:-1]
        elif c == '0':
            ans += '0'
        else:
            ans += '1'
    
    print(ans)

if __name__ == '__main__':
    main()