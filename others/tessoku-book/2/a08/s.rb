# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h
# A08 - Two Dimensional Sum

# ### 問題文
# H×W のマス目があります．上から i 行目，左から j 列目にあるマス (i,j) には，整数 Xi,j​ が書かれています．
# これについて，以下の Q 個の質問に答えるプログラムを作成してください．
# - i 個目の質問：左上 (Ai,Bi) 右下 (Ci,Di)) の長方形領域に書かれた整数の総和は？

# ### 制約
# - 1 ≤ H,W ≤ 1500
# - 1 ≤ Q ≤ 100000
# - 0 ≤ Xi,j ≤ 9
# - 1 ≤ Ai ≤ Ci ≤ H
# - 1 ≤ Bi ≤ Di ≤ W
# - 入力はすべて整数

h, w = gets.chomp.split.map(&:to_i)
x = h.times.map { gets.chomp.split.map(&:to_i) }
q = gets.to_i
abcd = q.times.map { gets.chomp.split.map(&:to_i) }

# 累積和を取る
prefix_sum = []
sum = [0] * w
h.times do |i|
  _sum = 0
  sum = [sum, x[i].map { _sum += _1 }].transpose.map(&:sum)
  prefix_sum << sum
end

abcd.each do |a, b, c, d|
  x = prefix_sum[c-1][d-1]
  y = [a-2, b-2].any? { _1 < 0 } ? 0 : prefix_sum[a-2][b-2]
  z = a-2 < 0 ? 0 : prefix_sum[a-2][d-1]
  aa = b-2 < 0 ? 0 : prefix_sum[b-2][c-1]
  puts x + y - z - aa
end
