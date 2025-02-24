"""
*    author:  kattsun
*    created: 24-02-2021 22:37:31
"""

def main():
    h,w = map(int, input().split())

    for i in range(h+2):
        if i == 0 or i == h + 1:
            print('#' * w + '##')
        else:
            print('#' + input().strip() + '#')
    

if __name__ == '__main__':
    main()