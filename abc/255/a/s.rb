r, c = gets.chomp.split.map(&:to_i)
a = 2.times.map { gets.chomp.split.map(&:to_i) }

puts a[r - 1][c - 1]
