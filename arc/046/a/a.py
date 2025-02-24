"""
*    author:  kattsun
*    created: 05-03-2021 08:19:02
"""

def main():
    n = int(input())
    cnt = 0
    x = 0

    while cnt < n:
        x += 1
        if len(set(list(str(x)))) == 1:
            cnt += 1
    print(x)    

if __name__ == '__main__':
    main()