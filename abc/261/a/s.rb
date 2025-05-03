L1, R1, L2, R2 = gets.chomp.split.map(&:to_i)

pp ([*L2...R2] & [*L1...R1]).size
