"""
*    author:  kattsun
*    created: 21-02-2021 22:06:11
"""

def main():
    a,b,c = map(int, input().split())
    a = int(str(a)[-1])
    if a in [2,3,7,8]:
        cycle = 4
    elif a in [4,9]:
        cycle = 2
    else:
        cycle = 1
    l = [[0],[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]

    bc = (b % cycle) ** (c % cycle) % cycle
    
    print(l[a][bc-1])

if __name__ == '__main__':
    main()