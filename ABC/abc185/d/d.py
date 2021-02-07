"""
*    author:  kattsun
*    created: 07-02-2021 10:00:08
"""
import math
def main():
    n,m = map(int, input().split())

    # マスが全部青色の場合ははんこを押さなくて良い
    if n-m == 0:
        print(0)
        return
    # 青色マスが0この場合は1回で全部の白色マスを押せる
    elif m == 0:
        print(1)
        return

    diff = [] # 青色マス間の距離

    # リストに両端を加える
    a = [0] + list(map(int, input().split())) + [n+1]
    a.sort()
    
    for i in range(m+1):
        d = a[i+1] - a[i] - 1
        if d != 0:
            diff.append(d)

    # 青色マスの間にはんこ(はんこ幅は青色マス間最小の幅)を押す回数
    k = min(diff)
    push = list(map(lambda v: math.ceil(v/k), diff))
    print(sum(push))

if __name__ == '__main__':
    main()