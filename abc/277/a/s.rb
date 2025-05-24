n, x = gets.chomp.split.map(&:to_i)
p = gets.chomp.split.map(&:to_i)

puts p.index(x) + 1
