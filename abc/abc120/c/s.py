"""
*    author:  kattsun
*    created: 23-04-2021 08:05:35
"""

def main():
    S = input().strip()
    cnt = {'0': 0, '1': 0}
    for c in S:
        if c == '0':
            cnt['0'] += 1
        else:
            cnt['1'] += 1
    print(min(cnt.values()) * 2)

if __name__ == '__main__':
    main()