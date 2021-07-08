"""
*    author:  kattsun
*    created: 09-07-2021 07:21:42
"""
def base_10_to_n(N,base):
    # コーナーケース
    if N == 0:
        return '0'

    ans = ''
    while N > 0:
        c = str(N % base)
        ans = c + ans
        N //= base
    ans = list(ans)
    return ans

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if '7' not in str(i) and '7' not in base_10_to_n(i, 8):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()