"""
*    author:  kattsun
*    created: 06-02-2021 20:57:57
"""

def main():
    v,t,s,d = list(map(int, input().split()))
    b = d/v

    if t <= b <= s:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()