"""
*    author:  kattsun
*    created: 23-02-2021 21:55:10
"""

def main():
    x,t = map(int, input().split())
    
    print(max(x-t,0))

if __name__ == '__main__':
    main()