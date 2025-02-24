"""
*    author:  kattsun
*    created: 19-02-2021 08:33:39
"""

def main():
    n,m = map(int, input().split())
    s = []  # 生徒
    cp = [] # チェックポイント

    for _ in range(n):
        s.append(list(map(int, input().split())))
    for _ in range(m):
        cp.append(list(map(int, input().split())))
    
    for i in s:
        x0, y0 = i
        ans = [0, 1000000000] # ポイント地点と、地点までの距離
        for j,p in enumerate(cp):
            x1,y1 = p
            diff = [j+1, abs(x0-x1) + abs(y0-y1)]
            if ans[1] > diff[1]:
                ans = diff
        print(ans[0])

if __name__ == '__main__':
    main()