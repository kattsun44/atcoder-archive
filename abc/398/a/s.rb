n = gets.to_i


center = n % 2 == 0 ? "==" : "="

puts "-" * ((n - 1) / 2) + center + "-" * ((n - 1) / 2)
