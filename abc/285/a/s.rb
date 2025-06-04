a, b = gets.chomp.split.map(&:to_i)

puts [a * 2, a * 2 + 1].include?(b) ? "Yes" : "No"
