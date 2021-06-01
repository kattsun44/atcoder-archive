"""
*    author:  kattsun
*    created: 01-06-2021 08:07:46
"""

def main():
    N = int(input())
    A = list(map(int, input().split()))
    free = 0
    color = set()
    for i in A:
        if i < 400:
            color.add('a')
        elif i < 800:
            color.add('b')
        elif i < 1200:
            color.add('c')
        elif i < 1600:
            color.add('d')
        elif i < 2000:
            color.add('e')
        elif i < 2400:
            color.add('f')
        elif i < 2800:
            color.add('g')
        elif i < 3200:
            color.add('h')
        else:
            free += 1
    print(max(1, len(color)), len(color) + free)
            

if __name__ == '__main__':
    main()