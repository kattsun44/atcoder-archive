"""
*    author:  kattsun
*    created: 14-05-2021 06:52:41
"""

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    exist = [0] * 201010
    for i in range(N):
        exist[P[i]] += 1
        while exist[ans]:
            ans += 1
        print(ans)

if __name__ == '__main__':
    main()