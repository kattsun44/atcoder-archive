require 'set'
n = gets.chomp.to_i
s = Set.new(n.times.map { gets.chomp })

pp s.size
