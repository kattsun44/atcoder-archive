"""
*    author:  kattsun
*    created: 02-08-2021 08:37:17
"""

def main():
    A, B, C = map(int, input().split())
    print(sum([A,B,C])-min([A,B,C]))

if __name__ == '__main__':
    main()