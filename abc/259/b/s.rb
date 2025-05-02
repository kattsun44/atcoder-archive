a, b, d = gets.chomp.split.map(&:to_i)

# 原点からの距離
r = Math.sqrt(a ** 2 + b ** 2)

# 原点からの初期座標の角度
x = Math.atan2(b, a)

# 変化後の角度
x2 = x + (d * Math::PI / 180)

puts [r * Math.cos(x2), r * Math.sin(x2)].join(" ")
