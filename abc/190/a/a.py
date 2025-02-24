"""
*    author:  kattsun
*    created: 30-01-2021 21:00:38
"""

def main():
    a,b,c = list(map(int, input().split(' ')))
    if a==b:
        if c==0:
            ans = 'Aoki'
        else:
            ans = 'Takahashi'
    elif a>b:
        ans = 'Takahashi'
    else:
        ans = 'Aoki'
    print(ans)

if __name__ == '__main__':
    main()