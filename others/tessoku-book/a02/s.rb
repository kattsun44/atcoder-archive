n, x = gets.chomp.split.map(&:to_i)
a = gets.chomp.split.map(&:to_i)

puts a.include?(x) ? "Yes" : "No"
