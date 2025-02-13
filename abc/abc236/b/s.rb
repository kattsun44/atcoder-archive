n = gets.to_i
a = gets.chomp.split(" ").map(&:to_i)

puts a.tally.select { |k, v| v == 3 }.keys
