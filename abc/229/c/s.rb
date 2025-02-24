n, w = gets.chomp.split(" ").map(&:to_i)

# Aの降順に並べる
a, b = n.times.map { gets.chomp.split(" ").map(&:to_i) }.sort.reverse.transpose

now, ans = w, 0 # 現在の重さ, 答え

n.times do |i|
  # w[g] 使い切っている場合はループを抜ける
  break if now <= 0

  # 現在の重さとチーズの総量を比較し、軽い方で計算する
  ans += a[i] * [now, b[i]].min

  # 使った分マイナスする
  now -= b[i]
end

puts ans
