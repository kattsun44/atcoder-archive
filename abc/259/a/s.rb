_, m, x, t, d = gets.chomp.split.map(&:to_i)

puts t - [x - m, 0].max * d
