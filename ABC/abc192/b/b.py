"""
*    author:  kattsun
*    created: 20-02-2021 21:07:03
"""

def main():
    s = input().strip()

    for i,c in enumerate(s):
        if i % 2 == 0:
            if c.isupper():
                print('No')
                return
        else:
            if c.islower():
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()