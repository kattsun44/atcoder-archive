"""
*    author:  kattsun
*    created: 27-02-2021 20:58:34
"""

def main():
    a,b = map(int, input().split())
    
    print((1-(b/a)) * 100)

if __name__ == '__main__':
    main()