"""
*    author:  kattsun
*    created: 09-06-2021 07:34:13
"""

def main():
    N = int(input())
    C = []
    C_i0 = [] # 各行0番目の値のリスト
    for i in range(N):
        C.append(list(map(int, input().split())))
        C_i0.append(C[i][0])
    m = min(C_i0)
    A = []
    for i in range(N):
        A.append(C[i][0]-m)
    B = []
    for i in range(N):
        B.append(C[0][i]-A[0])

    # 検証
    for i in range(N):
        for j in range(N):
            if C[i][j] != A[i] + B[j]:
                print('No')
                return
    print('Yes')
    print(' '.join(map(str,A)))
    print(' '.join(map(str,B)))

if __name__ == '__main__':
    main()