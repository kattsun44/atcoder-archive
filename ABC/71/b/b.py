"""
*    author:  kattsun
*    created: 16-01-2021 17:33:40
"""

def main():
    s = list(input().strip())
    atoz = [chr(i) for i in range(97, 123)]

    for i in atoz:
        if i not in s:
            print(i)
            return
    
    print('None')

if __name__ == '__main__':
    main()