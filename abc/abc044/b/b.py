"""
*    author:  kattsun
*    created: 13-04-2021 07:58:49
"""

def main():
    w = input().strip()
    cnt = dict()
    for c in w:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
    
    for a in cnt.values():
        if a % 2 != 0:
            print('No')
            return
    
    print('Yes')

if __name__ == '__main__':
    main()