"""
*    author:  kattsun
*    created: 09-04-2021 06:52:15
"""

def main():
    S = input().strip()
    ans = 0
    prev = ''
    now = ''

    for i in range(len(S)):
        now += S[i]
        if now == prev:
            continue
        else:
            ans += 1
            prev = now
            now = ''

    print(ans)

if __name__ == '__main__':
    main()