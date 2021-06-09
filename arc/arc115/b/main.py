"""
*    author:  kattsun
*    created: 09-06-2021 07:34:13
"""

def main():
    N = int(input())
    if N == 1:
        print('Yes')
        print(0)
        print(N)
        return
    C = []
    for i in range(N):
        C.append(list(map(int, input().split())))
    c_diff = []
    r_diff = []
    for i in range(N):
        if i != 0:
            r_diff.append(C[i][0]-C[i-1][0])
        for j in range(N-1):
            if i == 0:
                c_diff.append(C[i][j+1]-C[i][j])
            else:
                if C[i][j+1]-C[i][j] != c_diff[j]:
                    print('No')
                    return
    A = [0]
    B = [0]
    for i in range(N-1):
        A.append(A[i] + r_diff[i])
        B.append(B[i] + c_diff[i])
        minA = min(A)
        minB = min(B)
    for i in range(N):
        A[i] += -minA
        B[i] += C[i][0] - A[i]
    print('Yes')
    print(' '.join(map(str,A)))
    print(' '.join(map(str,B)))

if __name__ == '__main__':
    main()