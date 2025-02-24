"""
*    author:  kattsun
*    created: 15-05-2021 23:22:08
"""


def main():
    S = input().strip()
    ans = 0
    for i in range(10000):
        a = [0] * 10
        x = i
        for j in range(4):
            num = x % 10
            a[num] = 1
            x //= 10
        ok = True
        for j in range(10):
            if S[j] == 'o' and a[j] != 1:
                ok = False
            if S[j] == 'x' and a[j] != 0:
                ok = False
        if ok:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
