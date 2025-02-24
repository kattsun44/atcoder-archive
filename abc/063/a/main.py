"""
*    author:  kattsun
*    created: 14-06-2021 20:27:04
"""
import math
A, B = map(int, input().split())  # 2つ以上の数字

total = A + B

if total >= 10:
    print('error')
else:
    print(math.floor(total))
