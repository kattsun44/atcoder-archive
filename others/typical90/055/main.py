"""
*    author:  kattsun
*    created: 05-07-2021 07:12:58
"""
def main():
    N, P, Q = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    for m in range(l+1, N):
                        remainder = ((((A[i] * A[j])%P * A[k]%P) * A[l]%P) * A[m])%P
                        if remainder == Q:
                            ans += 1
    print(ans)

if __name__ == '__main__':
    main()