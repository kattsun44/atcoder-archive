"""
*    author:  kattsun
*    created: 04-07-2021 21:01:47
"""
import math
def main():
    P = int(input())
    cnt = 0
    remain = P
    for i in range(10,0,-1):
        fact = math.factorial(i)
        if remain >= fact:
            cnt += remain // fact
            remain = remain - fact * (remain // fact)
    print(cnt)

if __name__ == '__main__':
    main()