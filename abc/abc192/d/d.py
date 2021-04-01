"""
*    author:  kattsun
*    created: 20-02-2021 21:32:34
"""
import numpy as np
def main():
    x = input().strip()
    m = int(input())
    mx = max(list(map(int, list(x))))
    cnt = 0
    n = 0

    while True:
        for i in range(len(x)):
            n += int(x[i]) * (mx+1) ** (len(x)-i-1)
        print(n)
        cnt += 1
        mx += 1
        if n >= m:
            break
        n = 0
    
    print(cnt)

if __name__ == '__main__':
    main()