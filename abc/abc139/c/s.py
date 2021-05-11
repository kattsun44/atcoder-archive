"""
*    author:  kattsun
*    created: 12-05-2021 08:21:43
"""

def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    before = 0
    ans = 0

    for i in range(N):
      if H[i] <= before:
        cnt += 1
      else:
        cnt = 0
      ans = max(ans, cnt)
      before = H[i]

    print(ans)

if __name__ == '__main__':
    main()