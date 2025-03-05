n = gets.to_i
a = gets.chomp.split.map(&:to_i)

puts a.combination(3).map { _1.sum }.any? { _1 == 1000 } ? "Yes" : "No"
