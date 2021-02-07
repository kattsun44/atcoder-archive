"""
*    author:  kattsun
*    created: 07-02-2021 09:28:32
"""

def main():
    s = input().strip()
    t = input().strip()
    cnt = 0

    for i in range(len(s)):
        if s == t:
            print(cnt)
            return
        s = s[-1] + s[:-1]
        cnt += 1
    
    print(-1)

if __name__ == '__main__':
    main()