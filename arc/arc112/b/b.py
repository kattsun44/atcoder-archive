"""
*    author:  kattsun
*    created: 13-02-2021 22:44:47
"""

def main():
    b, c = map(int, input().split())
    ans = 0

    if b == 0:
        print(c)
        return

    if c <= b*2:
        ans += 1 + c # 内側
    else:
        if b < 0:
            ans += (abs(b) + 1) * 2
        else:
            ans += b * 2 + 1
    if c >= 3:
            ans += c - 2
    
    print(ans)

if __name__ == '__main__':
    main()