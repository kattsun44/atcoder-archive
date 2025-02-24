from collections import Counter
s = input().strip()
ans = 0
b_cnt = 0

# 'W' より左側にある 'B' を数える
for i in range(len(s)):
    if s[i] == 'B':
        b_cnt += 1
    if s[i] == 'W':
        ans += b_cnt


print(ans)