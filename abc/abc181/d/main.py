"""
*    author:  kattsun
*    created: 14-06-2021 07:29:17
"""
from collections import Counter
def main():
    S = input().strip()
    if len(S) <= 2:
        if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
        return
    
    cnt = Counter(S)

    for i in range(88 ,1000, 8):
        # Counter(str(i))-cnt == Counter() のとき Yes
        if not Counter(str(i))-cnt:
            print('Yes')
            return
    
    print('No')

if __name__ == '__main__':
    main()