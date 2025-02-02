n = gets.to_i
ans = 0
coordinates = n.times.map { gets.chomp.split(" ").map(&:to_i) }

coordinates.combination(3) do |a, b, c|
  # ベクトルの外積が0でない = 3点が直線上にない = 三角形
  ans += 1 if (b[0] - a[0]) * (c[1] - a[1]) != (b[1] - a[1]) * (c[0] - a[0])
end

pp ans
