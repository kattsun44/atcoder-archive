"""
*    author:  kattsun
*    created: 23-02-2021 20:42:47
"""

def main():
    s = input().strip()
    k = int(input())
    l = []
    cnt = 0
    ans = 0
    is_connect = False

    for i in range(len(s)):
        c = s[i]
        if i != 0:
            if pre_c != c:
                l.append(cnt)
                cnt = 0
        cnt += 1
        pre_c = c
    l.append(cnt)
    
    if s[0] == s[-1] and len(l) >= 2:
        is_connect = True
    
    for i in range(len(l)):
        ans += int(l[i]/2) * k
    
    if is_connect and l[0] % 2 == 1 and l[-1] % 2 == 1:
        ans += int(l[0]+l[-1]/2) * (k-1)

    print(ans)

if __name__ == '__main__':
    main()