n, m = gets.chomp.split.map(&:to_i)
a = gets.chomp.split.map(&:to_i).tally
b = gets.chomp.split.map(&:to_i).tally

puts b.each.all? { |k, v| a[k].to_i >= v } ? "Yes" : "No"
