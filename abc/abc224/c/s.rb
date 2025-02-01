n = gets.to_i

coordinates = n.times.map { gets.chomp.split(" ").map(&:to_i) }

ans = coordinates.combination(3).to_a.map(&:flatten).count do |x1, y1, x2, y2, x3, y3|
  # ベクトルの外積が0でない = 3点が直線上にない = 三角形
  (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)
end

pp ans
