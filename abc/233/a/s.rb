x, y = gets.chomp.split.map(&:to_i)

puts (y - x) < 0 ? 0 : ((y - x) / 10.0).ceil
