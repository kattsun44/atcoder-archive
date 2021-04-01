"""
*    author:  kattsun
*    created: 02-02-2021 20:07:02
"""

def main():
    s = input().strip()
    n = int(input())
    for i in range(n):
        l, r = map(int, input().split())

        p = s[l-1:r] # 部分文字列
        pr = ""      # 部分文字列の逆順
        for j in range(len(p)):
            pr += p[-(j+1)]

        s = s[:l-1] + pr + s[r:]

    print(s)

if __name__ == '__main__':
    main()