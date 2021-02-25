"""
*    author:  kattsun
*    created: 25-02-2021 22:45:16
"""

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    d = dict()
    a = sorted(a)
    sum = 0

    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    
    nums = 10000000 # 0から蓄積する数
    pkey = -1       # 1つ前のキー
    pnums = -1      # 1つ前のnums
    for key,value in d.items():
        # key がインクリメントする場合
        if key == pkey + 1:
            nums = min(k,value,nums)
        # key がインクリメントしない場合
        else:
            sum += nums * (pkey+1)
            print(sum)
            return
        # nums が減る場合にsumに加算
        if pnums > nums:
            sum += (pnums - nums) * key
        pkey = key
        pnums = nums
    
    sum += len(d) * nums
    print(sum)

if __name__ == '__main__':
    main()