"""
*    author:  kattsun
*    created: 23-01-2021 12:40:50
"""

def main():
    n = int(input())
    p = list(map(int, input().split(' ')))
    lowN = p[0]
    cnt = 0
    for i in p:
        if i <= lowN:
            lowN = i
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()