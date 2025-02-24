"""
*    author:  kattsun
*    created: 23-01-2021 21:01:29
"""

def main():
    s = input().strip()
    ans = 'Won' if len(set(s)) == 1 else 'Lost'
    print(ans)

if __name__ == '__main__':
    main()