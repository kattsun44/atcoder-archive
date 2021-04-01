"""
*    author:  kattsun
*    created: 16-01-2021 18:51:54
"""

def main():
    s = input().strip()
    
    print(s[0] + str(len(s)-2) + s[-1])

if __name__ == '__main__':
    main()