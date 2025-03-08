# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_g
# A07 - Event Attendance
# ある会社では D 日間にわたってイベントが開催され，N 人が出席します．
# 参加者 i は Li​ 日目から Ri​ 日目まで出席する予定です．
# 各日の出席者数を出力するプログラムを作成してください．

# 制約
# - 1 ≤ D,N ≤ 10^5
# - 1 ≤ L_i ≤ R_i ≤ D
# - 入力はすべて整数

d = gets.to_i
n = gets.to_i
l, r = n.times.map { gets.chomp.split(" ").map { _1.to_i - 1 } }.transpose

b = [0] * (d+1) # 最終日まで出席する人を考慮して+1日しておく

# 増減
n.times.map do |i|
  b[l[i]] += 1
  b[r[i]+1] -= 1 # 最終日の翌日にいなくなる
end

sum = 0
puts b[...-1].map { sum += _1 } # 最終日まで出力する
