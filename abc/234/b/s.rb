n = gets.to_i
coordinates = n.times.map { gets.chomp.split(" ").map(&:to_i) }

puts coordinates.combination(2).map { |a, b| Math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) }.max
