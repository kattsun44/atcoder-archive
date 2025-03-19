n = gets.to_i

nn = n >= 42 ? n + 1 : n

puts "AGC" + nn.to_s.rjust(3, "0")
