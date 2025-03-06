# 一次元の累積和
# N 日間にわたるイベント、Q 個の質問
n, q = gets.chomp.split.map(&:to_i)
# i 日目に A_i 人が来場
a = gets.chomp.split.map(&:to_i)
# L_{1..Q} 日目 から R_{1..Q} 日目
lr = q.times.map { gets.chomp.split.map { _1.to_i - 1 } }

# Q: 総来場者数は？
# A: まず累積和を求め、各期間についての来場者数は差分を出して求める

# 累積和
ps = [0] + n.times.map { a[0.._1].sum }

q.times do |i|
  l, r = lr[i][0], lr[i][1] + 1
  puts ps[r] - ps[l]
end
