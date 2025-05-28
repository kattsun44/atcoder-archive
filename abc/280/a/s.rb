h, w = gets.chomp.split.map(&:to_i)
s = h.times.map { gets.chomp }

pp s.join.count("#")
