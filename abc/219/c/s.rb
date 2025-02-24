x = gets
n = gets.to_i
s = n.times.map { gets.chomp }
puts s.sort_by { _1.tr(x, "a-z") }
