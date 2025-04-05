a, b, c = gets.chomp.split.map(&:to_i)

puts b == [a, b, c].sort[1] ? "Yes" : "No"
