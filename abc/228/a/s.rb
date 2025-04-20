s, t, x = gets.chomp.split.map(&:to_i)

range = s < t ? [s..t] : [s..24, 0..t]

puts range.any? { _1.cover?(x) } ? "Yes" : "No"
