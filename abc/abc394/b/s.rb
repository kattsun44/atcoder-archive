n = gets.to_i
s = n.times.map { gets.chomp }

puts s.sort_by { _1.size }.join
