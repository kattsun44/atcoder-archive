"""
*    author:  kattsun
*    created: 29-03-2021 08:25:12
"""
from itertools import product

def main():
    N = int(input())
    A = list(map(int, input().split()))
    INF = float('inf')
    ans = INF
    
    # bit全探索
    for _bit in product((True, False), repeat=N - 1):
        # 末尾はつねにTrueにする
        bit = list(_bit) + [True]
        # XOR、OR
        score, cur = [0, 0]
        
        for i in range(N):
            cur |= A[i]
            # 今のbitがTrueのとき、区間が終了するためscoreとcurを更新する
            if bit[i]:
                score ^= cur
                cur = 0
        ans = min(ans, score)
    
    print(ans)

if __name__ == '__main__':
    main()