"""
*    author:  kattsun
*    created: 12-02-2021 21:41:35
"""

def main():
    h,w = map(int, input().split())
    brd = []
    for i in range(h):
        brd.append(input().strip())
    
    for i in range(h):
        r = brd[i]
        print(r)
        print(r)

if __name__ == '__main__':
    main()