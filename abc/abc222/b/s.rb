n, p = gets.chomp.split(" ").map(&:to_i)
a = gets.chomp.split(" ").map(&:to_i).filter { |aa| aa < p }

puts a.length
