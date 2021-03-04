"""
*    author:  kattsun
*    created: 02-03-2021 22:08:15
"""

def main():
    o = input().strip()
    e = input().strip()
    ans = ''
    
    for i in range(len(o)):
        ans += o[i]
        if i != len(e):
            ans += e[i]
    
    print(ans)

if __name__ == '__main__':
    main()