a = gets.chomp.split.map(&:to_i).tally

puts a.values.count { _1 >= 2 } >= 2 && a.values.count { _1 >= 3} >= 1 ? "Yes" : "No"
