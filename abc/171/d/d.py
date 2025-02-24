"""
*    author:  kattsun
*    created: 11-02-2021 17:52:04
"""

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    chr_cnt = dict()
    for i in range(n):
        if a[i] in chr_cnt:
            chr_cnt[a[i]] += 1
        else:
            chr_cnt[a[i]] = 1
    pairs = []
    for k,v in chr_cnt.items():
        pairs.append([int(k), v])

    for i in range(q):
        b, c = map(int, input().split())
        s = 0
        for pair in pairs:
            if pair[0] == b:
                pair[0] = c
            s += pair[0] * pair[1]
        print(s)
    

if __name__ == '__main__':
    main()