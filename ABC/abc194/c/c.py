"""
*    author:  kattsun
*    created: 06-03-2021 21:13:10
"""
import itertools

def main():
    n = int(input())
    a = list(map(int, input().split()))
    comb = list(itertools.combinations(a, 2))
    ans = 0
    for i in range(len(comb)):
        x,y = comb[i]
        ans += (x-y)**2
    print(ans)

if __name__ == '__main__':
    main()