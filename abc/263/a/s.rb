a = gets.chomp.split.map(&:to_i)

puts a.tally.values.sort == [2, 3] ? "Yes" : "No"
