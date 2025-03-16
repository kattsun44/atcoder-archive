n, k = gets.chomp.split.map(&:to_i)
a = gets.chomp.split.map(&:to_i)
b = gets.chomp.split.map { _1.to_i - 1 }

puts a.values_at(*b).max == a.max ? "Yes" : "No"
