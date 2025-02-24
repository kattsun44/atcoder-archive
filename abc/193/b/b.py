"""
*    author:  kattsun
*    created: 27-02-2021 21:02:49
"""

def main():
    n = int(input())
    ans = -1

    for i in range(n):
        a,p,x = map(int, input().split())
        if x > a:
            if ans == -1:
                ans = p
            else:
                if p < ans:
                    ans = p
    
    print(ans)

if __name__ == '__main__':
    main()