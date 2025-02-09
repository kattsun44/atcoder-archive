n = gets.to_i
s = n.times.map { gets.chomp }

puts s.tally.sort_by(&:last).last[0]
