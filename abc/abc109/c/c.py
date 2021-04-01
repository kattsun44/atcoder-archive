"""
*    author:  kattsun
*    created: 18-03-2021 07:20:25
"""
import math

def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    INF = float('inf')
    ans = INF
    if x not in a:
        a.append(x)
        a.sort()
    for i in range(n):
        diff = a[i+1]-a[i]
        if i >= 1:
            ans = min(ans, math.gcd(diff, pref))
        else:
            ans = min(ans,diff)
        pref = diff
    print(ans)

if __name__ == '__main__':
    main()