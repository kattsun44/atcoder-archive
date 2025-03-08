# https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_al
# B07 - Convenience Store 2
# ### 問題文
# あるコンビニは時刻 0 に開店し、時刻 T に閉店します。
# このコンビニには N 人の従業員が働いており、i 番目 (1 ≤ i ≤ N) の従業員は時刻 Li​ に出勤し、時刻 Ri​ に退勤します。
# t=0,1,2,…,T−1 それぞれについて、時刻 t+0.5t+0.5 にコンビニにいる従業員の数を出力するプログラムを作成してください。

# ### 制約
# - 1 ≤ T ≤ 500000
# - 1 ≤ N ≤ 500000
# - 0 ≤ Li < Ri ≤ T (1 ≤ i ≤ N)
# - 入力はすべて整数

t = gets.to_i
n = gets.to_i
l, r = n.times.map { gets.chomp.split(" ").map { _1.to_i } }.transpose

diff = [0] * (t+1)

n.times do |i|
  diff[l[i]] += 1
  diff[r[i]] -= 1
end

sum = 0
puts diff[...-1].map { sum += _1 }
