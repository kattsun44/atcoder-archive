"""
*    author:  kattsun
*    created: 19-05-2021 07:26:56
"""

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt2 = 0
    cnt4 = 0
    cnt = 0
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 4 == 0:
                cnt4 += 1
            else:
                cnt2 += 1
        else:
            cnt += 1
    if cnt2 >= 1:
        cnt += 1
    if cnt <= cnt4 + 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()