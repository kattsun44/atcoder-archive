"""
*    author:  kattsun
*    created: 06-07-2021 07:03:10
"""
def base10int(N,base):
    ans = ''
    while N > 0:
        c = str(N % base)
        ans = c + ans
        N //= base
    ans = list(ans)
    return ans

def main():
    N8, K = map(int, input().split())
    # コーナーケース
    if N8 == 0:
        print(0)
        return

    for i in range(K):
        N10 = int(str(N8), 8)  # 8進数→10進数
        N9 = base10int(N10, 9) # 10進数→9進数
        N9 = ['5' if i == '8' else i for i in N9] # '8' を '5' に置換
        N8 = int(''.join(N9)) # 8進数とみなす

    print(N8)

if __name__ == '__main__':
    main()