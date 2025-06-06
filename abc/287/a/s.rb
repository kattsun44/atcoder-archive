n = gets.to_i
s = n.times.map { gets.chomp }

puts s.count { _1 == "For" } > n / 2 ? "Yes" : "No"
