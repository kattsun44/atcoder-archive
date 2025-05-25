n, k = gets.chomp.split.map(&:to_i)
a = gets.chomp.split.map(&:to_i)

puts (a + [0] * k)[k..].join(" ")
