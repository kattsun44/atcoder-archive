n = gets.to_i
a, b = [], []
n.times.map do
  ai, bi = gets.chomp.split(" ").map(&:to_i)
  a << ai
  b << bi
end

# 2つの火がぶつかる時刻
t = n.times.sum { |i| a[i] * 1.0 / b[i] * 1.0 } / 2.0

# 左の火が時刻 t においてどの地点に到達しているか
ans = 0
n.times do |i|
  ans += [a[i] * 1.0, t * b[i]].min
  t -= [a[i] * 1.0 / b[i] * 1.0, t].min
end

puts ans
