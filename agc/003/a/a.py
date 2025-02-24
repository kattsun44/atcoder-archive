"""
*    author:  kattsun
*    created: 12-03-2021 18:46:11
"""

def main():
    s = input().strip()
    D = set(list(s))
    sn = 0
    ew = 0
    for d in D:
        if d == 'S' or d == 'N':
            sn += 1
        else:
            ew += 1
    if sn % 2 == 0 and ew % 2 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()