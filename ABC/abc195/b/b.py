"""
*    author:  kattsun
*    created: 13-03-2021 21:01:54
"""

def main():
    a,b,w = map(int, input().split())
    inf = float('inf')
    mn = inf
    mx = -1
    cnt = 0
    jdg = False
    for i in range(a,b):
        c = w*1000//i # 軽い方の最大個数
        for j in range(c):
            cnt += j
            r = w*1000 - i*j
            cnt += round(r/b)
            mn = min(cnt,mn)
            mx = max(cnt,mx)
            cnt = 0
        if w*1000 - (i * j + round(r/b)*b) == 0:
            jdg = True
    
    if jdg:
        print(mn,mx)
    else:
        print('UNSATISFIABLE')

if __name__ == '__main__':
    main()