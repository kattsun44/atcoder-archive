"""
*    author:  kattsun
*    created: 16-03-2021 20:31:36
"""


def main():
    n, m = map(int, input().split())
    l = []
    r = []
    ans = 0
    for i in range(m):
        l0, r0 = map(int, input().split())
        l.append(l0)
        r.append(r0)
    ll = max(l)
    rr = min(r)

    if ll > rr:
        ans = 0
    else:
        ans = len(list(range(ll, rr)))+1
    print(ans)


if __name__ == '__main__':
    main()
