s1 = gets.chomp
s2 = gets.chomp
s3 = gets.chomp

puts ["ABC", "ARC", "AGC", "AHC"].reject { |a| [s1, s2, s3].include?(a) }
