"""
*    author:  kattsun
*    created: 03-02-2021 20:47:32
"""
import math
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = 0

    for i in range(n*2):
        if i % 2 == 1:
            total += a[i]

    print(total)

if __name__ == '__main__':
    main()