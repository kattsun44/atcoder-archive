a, b = gets.chomp.split.map(&:to_i)

puts b - a == 1 || b - a == 9 ? "Yes" : "No"
