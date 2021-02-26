"""
*    author:  kattsun
*    created: 26-02-2021 22:25:36
"""

def main():
    s = input().strip()
    w = 'keyence'
    cnt = 0

    for i in range(len(w)):
        if w[i] == s[i]:
            cnt += 1
        else:
            continue
    
    for i in range(len(w)):
        if w[(i+1)*-1] == s[(i+1)*-1]:
            cnt += 1
        else:
            continue
    
    if cnt >= 7:
        print('YES')
    else:
        print('NO')
        

if __name__ == '__main__':
    main()