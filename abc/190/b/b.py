"""
*    author:  kattsun
*    created: 30-01-2021 21:04:04
"""

def main():
    n,s,d = list(map(int, input().split(' ')))
    ans = 'No'
    for i in range(n):
        x,y = map(int, input().split(' '))
        if x<s and y>d:
            ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()